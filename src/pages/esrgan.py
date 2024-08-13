import streamlit as st
from model.esrgan import model
from src.components.uploader import uploader

def app():
    st.title("ESRGAN")
    st.link_button(url="https://github.com/xinntao/Real-ESRGAN", label="Github")

    uploader(model=model)
