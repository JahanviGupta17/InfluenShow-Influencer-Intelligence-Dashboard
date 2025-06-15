import streamlit as st
import pandas as pd

def upload_data():
    uploaded_file = st.file_uploader("Upload influencer data (.csv)", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state['df'] = df
        st.success("✅ Data uploaded successfully!")
