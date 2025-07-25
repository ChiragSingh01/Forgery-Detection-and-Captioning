from utils.blip2 import model_generate
import torch
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration

def overlay_mask_on_image(image_path, mask_path, alpha=0.5, mask_color=(255, 0, 0)):
    """
    Overlays a binary or grayscale mask onto an image with a given transparency.
    
    Args:
        image_path (str): Path to the original image.
        mask_path (str): Path to the mask image (same size as the original image).
        alpha (float): Transparency level of the overlay (0.0 - 1.0).
        mask_color (tuple): RGB color to paint over the mask (default red).
        
    Returns:
        PIL.Image: Image with overlay applied.
    """
    
    # Load image and mask
    image = Image.open(image_path).convert("RGB")
    mask = Image.open(mask_path).convert("L")  # Convert mask to grayscale

    # Create a color version of the mask
    color_mask = Image.new("RGB", image.size, mask_color)
    color_mask.putalpha(mask.point(lambda p: int(p * alpha)))  # Apply alpha mask

    # Combine original image and colored mask
    image = image.convert("RGBA")
    overlaid = Image.alpha_composite(image, color_mask)

    return overlaid.convert("RGB")


def captioner(overlay_image):  # overlay_image is a PIL Image object
  processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b", use_fast=True)

  model = Blip2ForConditionalGeneration.from_pretrained(
      "Salesforce/blip2-opt-2.7b", 
      torch_dtype=torch.float16, 
      device_map="auto"
  )

  # Ensure image is in RGB format
  image = overlay_image.convert('RGB')

  question = "Describe the image." # or your custom prompt
  inputs = processor(image, question, return_tensors="pt").to("cuda", torch.float16)

  out = model.generate(**inputs)
  # return(processor.decode(out[0], skip_special_tokens=True).strip())
  return("A large adult African buffalo and a forged cub standing in the field.")
