# components/report_export.py

import streamlit as st
import io

def download_report_builder(df):
    st.subheader("📁 Export Influencer Report")

    # Clean for export (optional: drop internal or temp cols)
    export_df = df.copy()
    export_buffer = io.StringIO()
    export_df.to_csv(export_buffer, index=False)
    csv_data = export_buffer.getvalue()

    st.download_button(
        label="📥 Download CSV",
        data=csv_data,
        file_name="influencer_report.csv",
        mime="text/csv",
        help="Download the processed influencer report as a CSV file."
    )
