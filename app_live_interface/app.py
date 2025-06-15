# influencer_dashboard/app.py
import streamlit as st
import pandas as pd
from components import upload, clean_profile, domain_detection, insight_generator, visualizer, report_export

st.set_page_config(page_title="Influencer Intelligence Dashboard", layout="wide")
st.title("🌐 Influencer Intelligence Dashboard")

st.sidebar.title("📂 Upload Data")
upload.upload_data()

if 'df' in st.session_state:
    df = st.session_state['df']

    # Clean and derive insights
    df = clean_profile.clean_columns(df)
    df = domain_detection.detect_content_domain(df)
    df = insight_generator.generate_derived_features(df)  # likes/followers, growth trend, fake follower score
    st.session_state['df'] = df

    # Main Visualizations
    visualizer.show_overview(df)
    visualizer.show_segmentation(df)
    visualizer.show_offer_analysis(df)
    visualizer.show_discovery_filters(df)  # Search & filter
    visualizer.show_ai_recommendations(df)  # OpenAI powered suggestions
    visualizer.show_score_ranking(df)  # influence_score & brand_fit_score
    visualizer.show_advanced_charts(df)  # radar, bubble, heatmap

    # Export
    report_export.download_report_builder(df)
else:
    st.info("📢 Upload a dataset to begin analysis.")
