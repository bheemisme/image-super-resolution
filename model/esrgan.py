import subprocess
from typing import List
from pathlib import Path

def model(input_files: List[Path]) -> List[Path]:
    output_files: List[Path] = []
    output_dir = Path('temp')
    model_path = Path("model/realesrgan-ncnn-vulkan-20220424-windows/realesrgan-ncnn-vulkan.exe")
    for input_file in input_files:
        output_file = output_dir / f"sr-{input_file.name}"
        output_file.touch()
        command = [str(model_path.absolute()), "-i", str(input_file.absolute()), "-o",
                       str(output_file.absolute()), "-n", "realesrgan-x4plus"]
        subprocess.run(command, capture_output=True, text=True)
        output_files.append(output_file)
    

    return output_files
