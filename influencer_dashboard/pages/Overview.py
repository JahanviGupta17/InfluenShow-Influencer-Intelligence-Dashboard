# pages/Overview.py

import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler
from utils.metrics import calculate_metrics

st.title("📊 Metrics Overview")

if 'df' in st.session_state:
    df = st.session_state['df']
    metrics_summary = calculate_metrics(df)

    # Top-level summary
    st.metric("Total Influencers", metrics_summary["total_influencers"])
    st.metric("Total Reach", metrics_summary["total_reach"])
    st.metric("Avg Engagement Rate", f"{metrics_summary['avg_eng_rate']:.2f}%")
    st.metric("High Performers", metrics_summary["high_performers"])

    st.subheader("📍 Influencer Radar: Normalized Profile Comparison")

    # Required columns
    required_cols = ['channel_id', 'avg_likes', '60_day_eng_rate', 'influence_score']
    if all(col in df.columns for col in required_cols):
        # Normalize metrics for radar
        radar_df = df.copy()
        scaler = MinMaxScaler()
        radar_df[['avg_likes', '60_day_eng_rate', 'influence_score']] = scaler.fit_transform(
            radar_df[['avg_likes', '60_day_eng_rate', 'influence_score']]
        )

        top5 = radar_df[['channel_id', 'avg_likes', '60_day_eng_rate', 'influence_score']].dropna().head(5)
        melted = top5.melt(id_vars='channel_id', var_name='Metric', value_name='value')

        fig = px.line_polar(
            melted,
            r='value',
            theta='Metric',
            color='channel_id',
            line_close=True,
            title="Top 5 Influencer Profiles (Radar Chart)"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Missing one or more required columns for radar chart.")
else:
    st.warning("⚠️ Please upload your dataset first.")
