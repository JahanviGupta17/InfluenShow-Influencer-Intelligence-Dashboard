# app.py
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from components import visualizer, llm_tab
import os

st.set_page_config(page_title="InfluenShow Dashboard", layout="wide")

# Load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")
load_dotenv()

st.title("🎯 InfluenShow – Influencer Intelligence Dashboard")

# 🔁 Column Normalization Logic
def normalize_columns(df):
    rename_map = {
        'channel_info': 'channel_id',
        'influencer_name': 'channel_id',
        'engagement_rate': '60_day_eng_rate',
        'niche': 'domain',
        'personalized_offer': 'offer_type'
    }
    df.columns = df.columns.str.strip().str.lower()
    df.rename(columns={k.lower(): v for k, v in rename_map.items()}, inplace=True)
    return df

# 📂 File uploader
uploaded_file = st.file_uploader("Upload influencer data (.csv)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df = normalize_columns(df)
    st.success("✅ Data uploaded and standardized!")

    tabs = st.tabs([
        "📊 Overview",
        "🧩 Segmentation",
        "🎯 Offer Analysis",
        "🔍 Discovery Filters",
        "🏆 Score Ranking",
        "📈 Charts",
        "🤖 LLM Advisor"
    ])

    with tabs[0]:
        st.markdown('<div class="fadein">', unsafe_allow_html=True)
        visualizer.show_overview(df)
        st.markdown('</div>', unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="fadein">', unsafe_allow_html=True)
        visualizer.show_segmentation(df)
        st.markdown('</div>', unsafe_allow_html=True)

    with tabs[2]: visualizer.show_offer_analysis(df)
    with tabs[3]: visualizer.show_discovery_filters(df)
    with tabs[4]: visualizer.show_score_ranking(df)
    with tabs[5]: visualizer.show_advanced_charts(df)
    with tabs[6]: llm_tab.show_llm_tab(df)

else:
    st.info("📁 Please upload a CSV file to get started.")
