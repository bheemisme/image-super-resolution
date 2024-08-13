import streamlit as st
from PIL import Image
import tempfile
from pathlib import Path

def uploader(model):

    input_images_path = Path("model\\input_images")
    # File uploader widget
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

    # Display details and content of uploaded files
    if uploaded_files:
        input_files = []



        for uploaded_file in uploaded_files:
            if uploaded_file.type == "image/jpeg" or uploaded_file.type == "image/png":
                with tempfile.NamedTemporaryFile(delete=False, dir=input_images_path) as tmp_file:
                    tmp_file.write(uploaded_file.read())
                    input_files.append(tmp_file)

        output_files = model(input_files)
        col1, col2 = st.columns(2)

        for i, o in zip(input_files, output_files):
            with col1:
                image = Image.open(i.name)
                st.image(image=image, caption="Input", use_column_width=True)

            with col2:
                image = Image.open(o.name+".png")
                st.image(image=image, caption="Output", use_column_width=True)

            @st.fragment
            def download():
                with open(o.name+".png", "rb") as file:
                    btn = st.download_button(
                        label="Download image",
                        data=file,
                        mime="image/png",
                    )
            download()
