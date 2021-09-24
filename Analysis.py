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

def convert_all_memes_to_text(meme_folder_path: str,
                              export_path):
    meme_names = os.listdir(meme_folder_path)

    for i in range(len(meme_names)):
        current_path = os.path.join(meme_folder_path, meme_names[i])
        converted_string = get_text(current_path)

        file = open(os.path.join(export_path, meme_names[i].replace(".png",".txt")), "a+", encoding = "utf-8")
        file.write(converted_string)
        file.close()
        print(i, "/", len(meme_names))

def get_saved_meme_text(text_meme_folder_path: str):

    for file_name in os.listdir(text_meme_folder_path):
        file = open(os.path.join(text_meme_folder_path, file_name), "r", encoding = "utf-8")
        print(file_name)
        print(file.read())
        file.close()

print(get_saved_meme_text(text_meme_folder_path = os.path.join("scraping", "exports")))

# print(convert_all_memes_to_text(os.path.join("scraping", "auto_download0"),
#                                 os.path.join("scraping", "exports")))

