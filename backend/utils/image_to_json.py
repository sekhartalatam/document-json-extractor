import pytesseract
from PIL import Image
import json

def image_to_json(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    data = {"text": text}
    return json.dumps(data, indent=4)
