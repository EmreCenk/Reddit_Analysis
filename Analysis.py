import os
import pytesseract
from dotenv import load_dotenv
from PIL import Image
load_dotenv()

tessPath = os.environ["tesseract_path"]
pytesseract.pytesseract.tesseract_cmd = tessPath

def get_text(image_path):
    try:
        return pytesseract.image_to_string(
            Image.open(image_path)
        )
    except:
        return -1

