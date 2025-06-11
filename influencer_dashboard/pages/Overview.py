import streamlit as st
import pandas as pd
from utils.metrics import calculate_metrics

st.title("📈 Metrics Overview")

if 'df' in st.session_state:
    df = st.session_state['df']
    metrics = calculate_metrics(df)

    st.metric("Total Influencers", metrics["total_influencers"])
    st.metric("Total Reach", metrics["total_reach"])
    st.metric("Avg Engagement Rate", f"{metrics['avg_eng_rate']:.2f}%")
    st.metric("High Performers", metrics["high_performers"])
else:
    st.warning("⚠️ Please upload the CSV from the main page first.")
