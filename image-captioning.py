from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
import torch

# Load pre-trained model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
img_path = "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg"
image = Image.open(requests.get(img_path, stream=True).raw).convert('RGB')
inputs = processor(image, return_tensors="pt")
output = model.generate(**inputs)

caption = processor.decode(output[0], skip_special_tokens=True)
print("Caption:", caption)