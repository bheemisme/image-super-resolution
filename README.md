
# Image Super Resolution

Structure

- `model` - model directory
- `src/pages` - pages of application
- `src/components` - components of application
- `environment` - app environment files

**Install requirements:**

```bash
pip install -r ./environment/requirements.txt
```

**To run:**

```bash
streamlit run ./main.py
```

Downalod model executable and place it in model directory without renaming

1. [Windows](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-windows.zip)
2. [Linux](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-ubuntu.zip)
3. [MacOS](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-macos.zip)

> create `input_images` and `output_images` directories in `model` directory.

### Deployment

[Click Here](https://bheemisme-image-super-resolution-main-a4fjs9.streamlit.app)
