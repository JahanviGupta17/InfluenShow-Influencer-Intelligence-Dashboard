import streamlit as st
import plotly.express as px
import pandas as pd

st.header("🎯 Offer Personalization")

if 'df' in st.session_state:
    df = st.session_state['df'].copy()

    # Basic sanity checks
    if "offer_type" not in df.columns:
        st.error("❌ Dataset must include an 'offer_type' column.")
    else:
        # Clean invalid entries
        df = df[df['offer_type'].notna()]
        df = df[~df['offer_type'].isin(['', 'N/A', 'unknown', '?'])]

        if df['offer_type'].nunique() == 0:
            st.warning("⚠️ No valid 'offer_type' entries found in the dataset.")
        else:
            st.subheader("📊 Campaign Offer Distribution")

            offer_counts = (
                df['offer_type']
                .value_counts()
                .rename_axis('offer_type')
                .reset_index(name='count')
            )

            fig = px.pie(
                offer_counts,
                names="offer_type",
                values="count",
                title="Offer Types in the Campaign"
            )
            st.plotly_chart(fig, use_container_width=True)

            # 🔹 Engagement Rate by Offer Type
            if "60_day_eng_rate" in df.columns:
                try:
                    df['60_day_eng_rate'] = (
                        df['60_day_eng_rate']
                        .astype(str)
                        .str.rstrip('%')
                        .astype(float)
                    )

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

            # 🔸 Offer Type by Segment (if segmentation done)
            if 'Segment' in df.columns:
                segment_offer = (
                    df.groupby(['Segment', 'offer_type'])
                    .size()
                    .reset_index(name='count')
                )

                st.subheader("📊 Offer Type Distribution by Segment")
                fig3 = px.bar(
                    segment_offer,
                    x='Segment',
                    y='count',
                    color='offer_type',
                    title="Offer Distribution per Influencer Segment",
                    barmode='stack'
                )
                st.plotly_chart(fig3, use_container_width=True)
else:
    st.warning("📂 Please upload a dataset to explore offer insights.")
