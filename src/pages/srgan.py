import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from model.srgan_cal import model
from src.components.uploader import uploader

# srgan page
def app():
    st.title("SRGAN")
    st.link_button(url="https://github.com/bheemisme/SRGAN", label="Github")

    st.markdown("### Training Results")
    df = pd.read_csv("./model/srgan/srf_4_train_results.csv", index_col='Epoch')
    
    fig, ax = plt.subplots(2, figsize=(8,10))
    x = np.linspace(0, 1.5, 90)
    ax[0].plot(x, df['Loss_D'])
    ax[0].plot(x, df['Loss_G'])
    ax[0].legend(labels=['Loss_D', 'Loss_G'])
    ax[0].set_title('Loss')

    ax[1].plot(x, df['Score_D'])
    ax[1].plot(x, df['Score_G'])
    ax[1].legend(labels=['Score_D', 'Score_G'])
    ax[1].set_title('Score')
    

    
    st.pyplot(fig)
    uploader(model=model)
