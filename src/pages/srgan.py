import streamlit as st
import pandas as pd
from model.srgan_cal import model
from src.components.uploader import uploader


def app():
    st.title("SRGAN")
    st.link_button(url="https://github.com/bheemisme/SRGAN", label="Github")

    st.markdown("### Training Results")
    df = pd.read_csv("./model/srgan/srf_4_train_results.csv", index_col='Epoch')
    
    st.write(df)

    uploader(model=model)
