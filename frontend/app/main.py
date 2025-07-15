# app.py

import streamlit as st
from frontend.app.pages.data_upload import render as upload_to_s3

# 🧭 Page routing logic
PAGES = {
    "📤 Upload File to S3": upload_to_s3,
    # Later you can add:
    # "📊 EDA Dashboard": eda_dashboard,
    # "🔍 Model Explainability": explainability_page,
}

st.set_page_config(page_title="AutoMLOps 360", layout="wide")
st.sidebar.title("🧭 Navigation")

selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.render()
