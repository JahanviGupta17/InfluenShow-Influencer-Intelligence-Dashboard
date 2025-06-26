# pages/segmentation.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.header("🧩 Influencer Segmentation")

if 'df' not in st.session_state:
    st.warning("📂 Please upload a dataset to explore segmentation.")
    st.stop()

df = st.session_state['df'].copy()

# Clean followers
try:
    df['followers'] = (
        df['followers']
        .astype(str)
        .str.replace(',', '', regex=False)
        .str.extract(r'(\d+)', expand=False)
        .astype(float)
    )
except Exception as e:
    st.error(f"❌ Could not process 'followers': {e}")
    st.stop()

# Segmentation
def segment_influencer(followers):
    if followers < 10_000:
        return 'Nano'
    elif followers < 100_000:
        return 'Micro'
    elif followers < 1_000_000:
        return 'Macro'
    else:
        return 'Mega'

df['Segment'] = df['followers'].apply(segment_influencer)
st.session_state['df'] = df  # Update with segment column

# 📊 Segment Counts
st.subheader("📊 Influencer Count by Segment")
segment_counts = df['Segment'].value_counts().reset_index()
segment_counts.columns = ['Segment', 'Count']
fig1 = px.bar(segment_counts, x='Segment', y='Count', color='Segment', title="Number of Influencers per Segment")
st.plotly_chart(fig1, use_container_width=True)

# 📈 Engagement by Segment
if '60_day_eng_rate' in df.columns:
    try:
        df['60_day_eng_rate'] = df['60_day_eng_rate'].astype(str).str.rstrip('%').astype(float)
        eng_rate_seg = df.groupby('Segment')['60_day_eng_rate'].mean().reset_index()
        st.subheader("📈 Avg Engagement Rate by Segment")
        fig2 = px.bar(eng_rate_seg, x='Segment', y='60_day_eng_rate', color='Segment')
        st.plotly_chart(fig2, use_container_width=True)
    except Exception as e:
        st.warning(f"⚠️ Error in engagement rate data: {e}")

# ❤️ Likes per Segment
if 'avg_likes' in df.columns:
    try:
        df['avg_likes'] = df['avg_likes'].astype(str).str.replace(',', '', regex=False).astype(float)
        likes_seg = df.groupby('Segment')['avg_likes'].mean().reset_index()
        st.subheader("❤️ Avg Likes per Post by Segment")
        fig3 = px.bar(likes_seg, x='Segment', y='avg_likes', color='Segment')
        st.plotly_chart(fig3, use_container_width=True)
    except Exception as e:
        st.warning(f"⚠️ Error in likes data: {e}")
