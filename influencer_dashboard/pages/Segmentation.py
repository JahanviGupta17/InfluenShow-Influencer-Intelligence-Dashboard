import streamlit as st
import pandas as pd
import plotly.express as px

st.header("🧩 Influencer Segmentation")

# ✅ Only run if dataset is uploaded
if 'df' in st.session_state:
    df = st.session_state['df'].copy()

    # 🧹 Clean 'followers' column
    try:
        df['followers'] = (
            df['followers']
            .astype(str)
            .str.replace(',', '', regex=False)
            .str.extract(r'(\d+)', expand=False)
            .astype(float)
        )
    except:
        st.error("❌ Could not convert 'followers' to numeric values. Check the data format.")
        st.stop()

    # 🔍 Segmentation logic
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
    st.session_state['df'] = df  # Save back segmented data

    # 📊 Influencer count by segment
    st.subheader("📊 Influencer Count by Segment")
    segment_counts = df['Segment'].value_counts().reset_index()
    segment_counts.columns = ['Segment', 'Count']
    fig1 = px.bar(segment_counts, x='Segment', y='Count', color='Segment', title="Number of Influencers per Segment")
    st.plotly_chart(fig1, use_container_width=True)

    # 📈 Avg. engagement rate per segment
    if '60_day_eng_rate' in df.columns:
        try:
            df['60_day_eng_rate'] = (
                df['60_day_eng_rate']
                .astype(str)
                .str.rstrip('%')
                .astype(float)
            )

            eng_rate_seg = (
                df.groupby('Segment')['60_day_eng_rate']
                .mean()
                .reset_index()
                .sort_values(by='60_day_eng_rate', ascending=False)
            )

            st.subheader("📈 Average 60-Day Engagement Rate by Segment")
            fig2 = px.bar(
                eng_rate_seg,
                x='Segment',
                y='60_day_eng_rate',
                color='Segment',
                title="Avg. Engagement (%) per Segment"
            )
            st.plotly_chart(fig2, use_container_width=True)

        except Exception as e:
            st.warning(f"⚠️ Could not process engagement rate data: {e}")

    # ❤️ Avg. likes per post per segment
    if 'avg_likes' in df.columns:
        try:
            df['avg_likes'] = (
                df['avg_likes']
                .astype(str)
                .str.replace(',', '', regex=False)
                .astype(float)
            )

            likes_seg = (
                df.groupby('Segment')['avg_likes']
                .mean()
                .reset_index()
                .sort_values(by='avg_likes', ascending=False)
            )

            st.subheader("❤️ Average Likes per Post by Segment")
            fig3 = px.bar(
                likes_seg,
                x='Segment',
                y='avg_likes',
                color='Segment',
                title="Avg. Likes per Post per Segment"
            )
            st.plotly_chart(fig3, use_container_width=True)

        except Exception as e:
            st.warning(f"⚠️ Could not process average likes data: {e}")

else:
    st.warning("📂 Please upload a dataset to explore segmentation.")
