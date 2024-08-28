from typing import List
from pathlib import Path

import torch
from PIL import Image
from torch.autograd import Variable
from torchvision.transforms import ToTensor, ToPILImage

from model.srgan.model import Generator

def model(input_files: List[Path]) -> List[Path]:
    output_files: List[Path] = []
    output_dir = Path("temp")
    model_path = Path("model/srgan/netG_epoch_4_10.pth")
    gen  = Generator(4).eval()
    gen.load_state_dict(torch.load(model_path , map_location=torch.device('cpu')))
    
    
    for input_file in input_files:
        output_file = output_dir / f"sr-{input_file.name}"
        output_file.touch()
        image = Image.open(input_file)
        image = Variable(ToTensor()(image)).unsqueeze(0)
        out = gen(image)
        out_img = ToPILImage()(out[0].data.cpu())
        out_img.save(output_file)
        output_files.append(output_file)

    return output_files
