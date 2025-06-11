import streamlit as st
import plotly.express as px
import pandas as pd

# ---------------------- HELPER FUNCTIONS ----------------------

def clean_engagement_string(val):
    if pd.isna(val) or not isinstance(val, str):
        return None
    try:
        parts = [p.strip().replace('%', '') for p in val.split('%') if p.strip() not in ['', '??']]
        floats = [float(p) for p in parts]
        return sum(floats) / len(floats) if floats else None
    except:
        return None

def segment_influencer(f):
    if f < 10_000:
        return 'Nano'
    elif f < 100_000:
        return 'Micro'
    elif f < 1_000_000:
        return 'Macro'
    else:
        return 'Mega'

# ---------------------- MAIN VISUALIZER FUNCTIONS ----------------------

def show_overview(df):
    st.subheader("📈 Metrics Overview")

    df['clean_eng_rate'] = df['60_day_eng_rate'].apply(clean_engagement_string)

    total_influencers = len(df)
    total_reach = df['followers'].sum()
    avg_engagement = df['clean_eng_rate'].mean()
    high_performers = df[df['clean_eng_rate'] > 5].shape[0]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Influencers", total_influencers)
    col2.metric("Total Reach", f"{total_reach:,.0f}")
    col3.metric("Avg Engagement Rate", f"{avg_engagement:.2f}%")
    col4.metric("High Performers", high_performers)

def show_segmentation(df):
    st.subheader("🧩 Influencer Segmentation")

    df['followers'] = (
        df['followers'].astype(str)
        .str.replace(',', '', regex=False)
        .str.extract(r'(\d+)', expand=False)
        .astype(float)
    )
    df['Segment'] = df['followers'].apply(segment_influencer)

    seg_counts = df['Segment'].value_counts().reset_index()
    seg_counts.columns = ['Segment', 'Count']

    st.plotly_chart(
        px.bar(seg_counts, x='Segment', y='Count', color='Segment', title="Segment Distribution"),
        use_container_width=True
    )

def show_offer_analysis(df):
    st.subheader("🎯 Offer Personalization")

    if 'offer_type' in df.columns:
        cleaned = df[df['offer_type'].notna() & ~df['offer_type'].isin(['', 'N/A', 'unknown'])]
        offer_counts = cleaned['offer_type'].value_counts().reset_index()
        offer_counts.columns = ['offer_type', 'count']

        fig = px.pie(offer_counts, names='offer_type', values='count', title="📊 Campaign Offer Distribution")
        st.plotly_chart(fig, use_container_width=True)

def show_discovery_filters(df):
    st.subheader("🔍 Influencer Discovery Filters")

    col1, col2 = st.columns(2)

    with col1:
        country = st.multiselect("Filter by Country", df['country'].dropna().unique())
        domain = st.multiselect("Filter by Domain", df['domain'].dropna().unique())

    with col2:
        min_followers, max_followers = st.slider("Follower Range", 0, int(df['followers'].max()), (0, int(df['followers'].max())))
        min_eng, max_eng = st.slider("Engagement Rate (%)", 0.0, 10.0, (0.0, 10.0))

    mask = (
        (df['followers'] >= min_followers) &
        (df['followers'] <= max_followers) &
        (df['clean_eng_rate'] >= min_eng) &
        (df['clean_eng_rate'] <= max_eng)
    )

    if country:
        mask &= df['country'].isin(country)
    if domain:
        mask &= df['domain'].isin(domain)

    filtered = df[mask]
    st.dataframe(filtered)

def show_ai_recommendations(df):
    st.subheader("🤖 AI-Powered Influencer Suggestions")

    domain = st.selectbox("Target Domain", df['domain'].dropna().unique())
    audience = st.text_input("Target Audience", "Gen Z females in India")

    if st.button("Suggest Influencers"):
        top_df = df[(df['domain'] == domain)].sort_values(by='clean_eng_rate', ascending=False).head(5)
        st.write(f"Top 5 Influencers in **{domain}** for **{audience}**:")
        st.dataframe(top_df[['channel_info', 'followers', 'clean_eng_rate']])

def show_score_ranking(df):
    st.subheader("🏆 Influence & Brand Fit Scores")

    if 'influence_score' not in df.columns:
        df['influence_score'] = (df['followers'] * df['clean_eng_rate']) / 10000

    if 'brand_fit_score' not in df.columns:
        df['brand_fit_score'] = (df['influence_score'] * 0.8).round(2)

    st.dataframe(
        df[['channel_info', 'followers', 'clean_eng_rate', 'influence_score', 'brand_fit_score']]
        .sort_values(by='influence_score', ascending=False)
        .head(10)
    )

def show_advanced_charts(df):
    st.subheader("📊 Advanced Visual Analytics")

    # Ensure Segment column exists
    if 'Segment' not in df.columns:
        def segment_influencer(f):
            if f < 10_000:
                return 'Nano'
            elif f < 100_000:
                return 'Micro'
            elif f < 1_000_000:
                return 'Macro'
            else:
                return 'Mega'
        df['Segment'] = df['followers'].apply(segment_influencer)

    # Radar Chart: Top 5 influencers with complete data
    radar_df = df[['channel_info', 'clean_eng_rate', 'avg_likes', 'influence_score']].dropna().head(5)
    if not radar_df.empty:
        radar_df = radar_df.set_index('channel_info').T
        st.line_chart(radar_df)
    else:
        st.warning("Not enough data for radar chart.")

    # Bubble Chart: Filter rows without NaNs in critical columns
    bubble_df = df[['followers', 'clean_eng_rate', 'avg_likes', 'channel_info', 'Segment']].dropna()

    if bubble_df.empty:
        st.warning("Not enough data for bubble chart.")
        return

    fig = px.scatter(
        bubble_df,
        x='followers',
        y='clean_eng_rate',
        size='avg_likes',
        hover_name='channel_info',
        color='Segment',
        title="Followers vs Engagement Rate vs Avg Likes"
    )
    st.plotly_chart(fig, use_container_width=True)
