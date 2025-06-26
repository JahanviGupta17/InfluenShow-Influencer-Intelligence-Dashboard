import streamlit as st
import pandas as pd

def upload_data():
    uploaded_file = st.file_uploader("Upload influencer data (.csv)", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        # ✅ Rename column if necessary
        if "channel_id" not in df.columns and "channel_info" in df.columns:
            df = df.rename(columns={"channel_info": "channel_id"})

        # ✅ Optional: Remove extra spaces or casing issues
        df.columns = df.columns.str.strip()

        st.session_state['df'] = df
        st.success("✅ Data uploaded successfully!")
