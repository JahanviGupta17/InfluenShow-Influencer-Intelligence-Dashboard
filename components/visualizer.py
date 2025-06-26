import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_extras.stylable_container import stylable_container

# ---------------------- SEGMENTATION & METRICS ----------------------

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
    st.markdown('<div class="fadein">', unsafe_allow_html=True)
    st.subheader("📈 Metrics Overview")

    df['followers'] = pd.to_numeric(df['followers'], errors='coerce')

    if '60_day_eng_rate' not in df.columns:
        st.warning("Missing '60_day_eng_rate' column.")
        st.markdown('</div>', unsafe_allow_html=True)
        return

    df['60_day_eng_rate'] = df['60_day_eng_rate'].astype(str).str.replace('%', '', regex=False)

    def extract_and_avg(cell):
        try:
            numbers = [float(x) for x in cell.replace(' ', '').split('%') if x.strip() != '']
            if not numbers:
                numbers = [float(x) for x in cell.split() if x.strip() != '']
            return sum(numbers) / len(numbers) if numbers else None
        except:
            return None

    df['60_day_eng_rate_clean'] = df['60_day_eng_rate'].apply(extract_and_avg)

    avg_engagement = df['60_day_eng_rate_clean'].mean()
    total_influencers = len(df)
    total_reach = df['followers'].sum()
    high_performers = df[df['60_day_eng_rate_clean'] > 5].shape[0]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Influencers", total_influencers)
    col2.metric("Total Reach", f"{total_reach:,.0f}")
    col3.metric("Avg Engagement Rate", f"{avg_engagement:.2f}%")
    col4.metric("High Performers", high_performers)

    st.markdown('</div>', unsafe_allow_html=True)

def show_segmentation(df):
    st.subheader("🧹 Influencer Segmentation")
    df['followers'] = pd.to_numeric(df['followers'], errors='coerce')
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

    df['followers'] = pd.to_numeric(df['followers'], errors='coerce')
    df['60_day_eng_rate'] = pd.to_numeric(df['60_day_eng_rate'], errors='coerce')

    max_followers_val = df['followers'].max()
    max_followers_val = int(max_followers_val) if pd.notna(max_followers_val) else 1_000_000

    col1, col2 = st.columns(2)

    with col1:
        countries = df['country'].dropna().unique()
        domains = df['domain'].dropna().unique()
        country = st.multiselect("Filter by Country", sorted(countries))
        domain = st.multiselect("Filter by Domain", sorted(domains))

    with col2:
        min_followers, max_followers = st.slider("Follower Range", 0, max_followers_val, (0, max_followers_val))
        min_eng, max_eng = st.slider("Engagement Rate (%)", 0.0, 10.0, (0.0, 10.0))

    mask = (
        df['followers'].between(min_followers, max_followers, inclusive="both") &
        df['60_day_eng_rate'].between(min_eng, max_eng, inclusive="both")
    )
    if country:
        mask &= df['country'].isin(country)
    if domain:
        mask &= df['domain'].isin(domain)

    filtered = df[mask]
    if filtered.empty:
        st.warning("No influencers found with selected filters.")
    else:
        st.dataframe(filtered.reset_index(drop=True))

def show_score_ranking(df):
    st.subheader("🏆 Influence & Brand Fit Scores")

    df['followers'] = pd.to_numeric(df['followers'], errors='coerce')
    df['60_day_eng_rate'] = pd.to_numeric(df['60_day_eng_rate'], errors='coerce')

    if 'channel_id' not in df.columns:
        st.error("Missing 'channel_id' in data.")
        return
    if 'influence_score' not in df.columns:
        df['influence_score'] = (df['followers'] * df['60_day_eng_rate']) / 10000

    if 'brand_fit_score' not in df.columns:
        df['brand_fit_score'] = (df['influence_score'] * 0.8).round(2)

    display_cols = ['channel_id', 'followers', '60_day_eng_rate', 'influence_score', 'brand_fit_score']
    available_cols = [col for col in display_cols if col in df.columns]
    st.dataframe(df[available_cols].sort_values(by='influence_score', ascending=False).head(10))

def show_advanced_charts(df):
    st.subheader("📊 Advanced Visual Analytics")

    df['followers'] = pd.to_numeric(df['followers'], errors='coerce')
    if 'Segment' not in df.columns:
        df['Segment'] = df['followers'].apply(segment_influencer)

    radar_df = df[['channel_id', '60_day_eng_rate', 'avg_likes', 'influence_score']].dropna().head(5)
    if not radar_df.empty:
        melted = radar_df.melt(id_vars='channel_id', var_name='Metric', value_name='value')
        fig = px.line_polar(
            melted,
            r='value',
            theta='Metric',
            color='channel_id',
            line_close=True,
            title="📍 Influencer Profile Radar (Top 5 Normalized)"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Not enough data for radar chart.")

    st.subheader("📊 Segment-wise Engagement vs Likes")
    heatmap_df = df[['Segment', 'avg_likes', '60_day_eng_rate']].dropna()

    if not heatmap_df.empty:
        grouped = heatmap_df.groupby('Segment').agg(
            avg_likes=('avg_likes', 'mean'),
            avg_eng_rate=('60_day_eng_rate', 'mean')
        ).reset_index()

        fig = px.scatter(
            grouped,
            x='avg_likes',
            y='avg_eng_rate',
            color='Segment',
            size='avg_eng_rate',
            text='Segment',
            title="Average Likes vs Engagement Rate per Segment"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Not enough data for segment-wise chart.")
