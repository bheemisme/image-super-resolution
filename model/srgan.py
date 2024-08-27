import subprocess
import tempfile
from typing import List
from pathlib import Path

def model(input_files: List[tempfile._TemporaryFileWrapper]) -> List[tempfile._TemporaryFileWrapper]:
    output_files = []
    output_dir = 'model/output_images'
    model_path = "model/srgan/test_image.py"
    for input_file in input_files:
        
        with tempfile.NamedTemporaryFile(dir=output_dir, delete=False) as output:
            command = ["python" , model_path,  "--model_name", "netG_epoch_4_10.pth", "--image_name", input_file.name, "--test_mode", "CPU"]
            subprocess.run(command, capture_output=True, text=True)
            output_files.append(output)

    return output_files
