# Team Members:
# Sudarshan
# Tinu Anand
# Rohitt

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
    model_path = Path("model/srgan/netG_epoch_4_90.pth") # path of the model
    gen  = Generator(4).eval() # initialising the model

    # loading the model
    gen.load_state_dict(torch.load(model_path , map_location=torch.device('cpu'), weights_only=True))
    
    
    # taking the input files from streamlit drop in
    
    for input_file in input_files:
        output_file = output_dir / f"sr-{input_file.name}"
        output_file.touch()
        image = Image.open(input_file)
        image = Variable(ToTensor()(image)).unsqueeze(0)
        out = gen(image) # passing the image to model and getting enhanced image
        out_img = ToPILImage()(out[0].data.cpu())
        out_img.save(output_file)
        output_files.append(output_file)

    # returning all enhanced images
    return output_files
