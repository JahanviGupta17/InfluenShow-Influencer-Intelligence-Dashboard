# pages/offers.py

import streamlit as st
import plotly.express as px
from components.llm_brand_suitability import build_influencer_context, get_brand_suitability
import pandas as pd

st.header("🎯 Offer Personalization")

if 'df' not in st.session_state:
    st.warning("📂 Please upload a dataset to explore offer insights.")
    st.stop()

df = st.session_state['df']

# LLM Analysis Variables (set by user in sidebar or elsewhere)
target_domain = st.session_state.get('target_domain', 'General')
target_audience = st.session_state.get('target_audience', 'Young adults')
run_llm = st.session_state.get('run_suitability', False)

# 👉 Suitability Analysis (LLM)
if run_llm:
    st.subheader("📋 Brand Suitability Insights (LLM-Powered)")
    top_influencers = df.sort_values(by='influence_score', ascending=False).head(5)

    for i, row in top_influencers.iterrows():
        profile_text = build_influencer_context(row)
        with st.spinner(f"Analyzing @{row.get('channel_id', f'user_{i+1}')}..."):
            suitability = get_brand_suitability(profile_text, target_domain, target_audience)

        st.markdown(f"### 🧑‍💼 @{row.get('channel_id', f'user_{i+1}')}")
        st.write(f"**Domain**: {row['domain']} | **Followers**: {row['followers']} | **Offer Type**: {row['offer_type']}")
        st.info(suitability)

# ------------------------
# 📊 Offer Analytics Section
# ------------------------

if "offer_type" not in df.columns:
    st.error("❌ Dataset must include an 'offer_type' column.")
    st.stop()

# Clean offer_type
df = df[df['offer_type'].notna()]
df = df[~df['offer_type'].isin(['', 'N/A', 'unknown', '?'])]

if df['offer_type'].nunique() == 0:
    st.warning("⚠️ No valid 'offer_type' entries found in the dataset.")
else:
    st.subheader("📊 Campaign Offer Distribution")

    offer_counts = df['offer_type'].value_counts().reset_index()
    offer_counts.columns = ['offer_type', 'count']

    fig = px.pie(offer_counts, names='offer_type', values='count', title="Offer Types in the Campaign")
    st.plotly_chart(fig, use_container_width=True)

    # Avg Engagement Rate by Offer Type
    if "60_day_eng_rate" in df.columns:
        try:
            df['60_day_eng_rate'] = df['60_day_eng_rate'].astype(str).str.rstrip('%').astype(float)

            engagement_avg = (
                df.groupby('offer_type')['60_day_eng_rate']
                .mean()
                .reset_index()
                .sort_values(by='60_day_eng_rate', ascending=False)
            )

            st.subheader("📈 Average Engagement Rate by Offer Type")
            fig2 = px.bar(
                engagement_avg,
                x='offer_type',
                y='60_day_eng_rate',
                color='offer_type',
                title="Avg. Engagement Rate (%) per Offer Type"
            )
            st.plotly_chart(fig2, use_container_width=True)
        except Exception as e:
            st.warning(f"Could not process engagement rate data: {e}")

    # Segment breakdown
    if 'Segment' in df.columns:
        segment_offer = df.groupby(['Segment', 'offer_type']).size().reset_index(name='count')
        st.subheader("📊 Offer Type Distribution by Segment")
        fig3 = px.bar(
            segment_offer,
            x='Segment',
            y='count',
            color='offer_type',
            barmode='stack',
            title="Offer Distribution per Influencer Segment"
        )
        st.plotly_chart(fig3, use_container_width=True)
