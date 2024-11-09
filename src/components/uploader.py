# Team Members:
# Sudarshan
# Tinu Anand
# Rohitt

from typing import List
import streamlit as st
from PIL import Image
from pathlib import Path

# component for uploading the images
def uploader(model):

    input_images_dir = Path("temp")
    # File uploader widget
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

    # Display details and content of uploaded files
    if uploaded_files:
        input_files: List[Path] = []

        for uploaded_file in uploaded_files:
            if uploaded_file.type == "image/jpeg" or uploaded_file.type == "image/png":
                
                with open(input_images_dir / uploaded_file.name, "wb") as input_file:
                    input_file.write(uploaded_file.read())
                    input_files.append(Path(input_file.name))

        output_files: List[Path] = model(input_files)
        col1, col2 = st.columns(2)

        for i, o in zip(input_files, output_files):
            
            with col1:
                image = Image.open(i)
                st.image(image=image, caption="Input", use_column_width=True)

            with col2:
                image = Image.open(o)
                st.image(image=image, caption="Output", use_column_width=True)
