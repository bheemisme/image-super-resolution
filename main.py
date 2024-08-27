import streamlit as st
from src.pages import esrgan, srgan

# A dictionary to map page names to their respective modules
PAGES = {
    "srgan": srgan,
    "esrgan": esrgan,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
if selection is not None:
    page = PAGES[selection]
    page.app()
