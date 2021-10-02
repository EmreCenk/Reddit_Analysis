import copy
import os
import pytesseract
from dotenv import load_dotenv
from PIL import Image
from typing import List
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

def get_saved_meme_text(text_meme_folder_path: str) -> List[str]:
    text_list = []
    for file_name in os.listdir(text_meme_folder_path):
        file = open(os.path.join(text_meme_folder_path, file_name), "r", encoding = "utf-8")
        text_list.append(file.read())
        file.close()
    return text_list

def get_all_words(text_meme_folder_path: str):
    all_text = get_saved_meme_text(text_meme_folder_path = text_meme_folder_path)
    all_words = []
    for t in all_text:
        t = t.split("\n")
        for i in range(len(t)):
            for j in t[i].split(" "):
                if j in {",", ".", " ", "", ":", '!', '"', '#',
                         '$', '%', '&', "'", '(', ')', '*', '+',
                         ',', '-', '.', '/', ':', ';', '<',
                         '=', '>', '?', '@', '[', r'\\', ']',
                         '^', '_', '`', '{', '|', '}', '~', '/',
                         r'\ '[:-1], "'", "`",
                         '0', '1', '2', '3', '4', '5', '6',
                         '7', '8', '9'}:
                    continue
                all_words.append(j)

    return all_words
def count_list(list_of_words):
    counted = {}
    for w in list_of_words:
        w = w.lower()
        if w in counted:
            counted[w] += 1
        else:
            counted[w] = 1
    return counted

def get_scraped_sorted_words():
    """Counting words from the scraped data, then sorting by occurence:"""
    word_list = get_all_words(os.path.join("scraping", "exports"))
    counted = count_list(word_list)

    sortCount = sorted(counted, key=lambda element: counted[element])
    # for k in sortCount:
    #     print(k, counted[k])
    return sortCount, counted
if __name__ == '__main__':
    print(get_scraped_sorted_words())

    # print(convert_all_memes_to_text(os.path.join("scraping", "auto_download1"),
    #                                 os.path.join("scraping", "exports")))

