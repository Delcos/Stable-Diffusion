# Hello and welcome to the pure stable diffusion experince. If you are missing anything simply use pip to download them. If you get something missing just type "pip install PACKAGENAMEHERE" without the " .
from diffusers import StableDiffusionPipeline
import torch
import time

print("Hello and welcome to the pure Stable Diffusion 2.0 experinece.")

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

def start() :
    timestr = time.strftime("%Y%m%d-%H%M%S")
    prompt = input("Enter your value: ")
    image = pipe(prompt).images[0]
    image.save("{}.png".format(timestr))

invalid_input = True
while invalid_input:
    start()







