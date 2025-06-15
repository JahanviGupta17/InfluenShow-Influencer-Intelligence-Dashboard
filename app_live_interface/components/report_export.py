import streamlit as st

def download_report_builder(df):
    st.subheader("📁 Export Influencer Report")
    st.download_button(
        label="📥 Download CSV",
        data=df.to_csv(index=False),
        file_name="influencer_report.csv",
        mime="text/csv"
    )
