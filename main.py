# Team Members:
# Sudarshan
# Tinu Anand
# Rohitt

import streamlit as st
from src.pages import esrgan, srgan
from download_model import download_file

# Example usage:
download_file()

# A dictionary to map page names to their respective modules
PAGES = {
    "srgan": srgan,
    "esrgan": esrgan,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# initialising the app
if selection is not None:
    page = PAGES[selection]
    page.app()
