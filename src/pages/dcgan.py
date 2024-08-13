import streamlit as st


from model.esrgan import model
from src.components.uploader import uploader



def app():
    st.title("DCGAN")
    st.link_button(url="https://github.com/Lornatang/DCGAN-PyTorch", label="Github")

    uploader(model=model)
