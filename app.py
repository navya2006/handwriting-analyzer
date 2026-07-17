import requests
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
from IPython.display import display

processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

def show_image(pathStr):
    img = Image.open(pathStr).convert("RGB")
    display(img)
    return img

def ocr_image(scrImg):
    pixel_values = processor(images=scrImg, return_tensors="pt").pixel_values.to(model.device)
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text

hw_image = show_image('process.jpeg')

text = ocr_image(hw_image)
print("Recognized text:")
print(text)

hw_img2 = hw_image.crop((0,))