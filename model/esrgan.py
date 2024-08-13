import subprocess
import tempfile
from typing import List
from pathlib import Path

def model(input_files: List[tempfile._TemporaryFileWrapper]) -> List[tempfile._TemporaryFileWrapper]:
    output_files = []
    output_dir = 'model\\output_images'
    model_path = "model\\realesrgan-ncnn-vulkan-20220424-windows\\realesrgan-ncnn-vulkan.exe"
    for input_file in input_files:
        with tempfile.NamedTemporaryFile(dir=output_dir, delete=False) as output:
            command = [model_path, "-i", input_file.name, "-o",
                       output.name + ".png", "-n", "realesrgan-x4plus"]
            subprocess.run(command, capture_output=True, text=True)
            output_files.append(output)

    return output_files
