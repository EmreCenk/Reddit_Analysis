import copy
import os
import pytesseract
from dotenv import load_dotenv
from PIL import Image
from typing import List, Tuple, Dict
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

def erase_occurences(word:str, list_of_words: List, what_to_replace_with: str = ""):
    new_word = str(word)
    for i in range(len(list_of_words)):
        new_word = new_word.replace(list_of_words[i], what_to_replace_with)
    return new_word
def get_all_words(text_meme_folder_path: str):
    to_replace = [",", ".", " ", "", ":", '!', '"', '#',
                  '$', '%', '&', "'", '(', ')', '*', '+',
                  ',', '-', '.', '/', ':', ';', '<',
                  '=', '>', '?', '@', '[', r'\\', ']',
                  '^', '_', '`', '{', '|', '}', '~', '/',
                  r'\ '[:-1], "'", "`", "‘", "‘", "'",
                  '0', '1', '2', '3', '4', '5', '6',
                  '7', '8', '9', '"']

    all_text = get_saved_meme_text(text_meme_folder_path = text_meme_folder_path)
    all_words = []
    for t in all_text:
        t = t.split("\n")
        for i in range(len(t)):
            for j in t[i].split(" "):
                j = erase_occurences(j, to_replace)
                if j == "":
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

def get_scraped_sorted_words() -> Tuple[List[str], Dict[str, int]]:
    """Counting words from the scraped data, then sorting by occurence:"""
    word_list = get_all_words(os.path.join("scraping", "exports"))
    counted = count_list(word_list)

    sortCount = sorted(counted, key=lambda element: counted[element])
    # for k in sortCount:
    #     print(k, counted[k])
    return sortCount, counted

def get_english_common_words(path: str = "scraping/data_sets/english_common_words.csv") -> Tuple[List[str], Dict[str, int]]:
    file = open(path, "r")
    info = file.read().split("\n")
    file.close()

    word_to_index = {}
    word_list = []
    for i in range(len(info)):
        current_split = info[i].split(";")
        try:
            current_split[0] = int(current_split[0])
            word_to_index[current_split[1]] = current_split[0] - 1
            word_list.append(current_split[1])



        except: pass #the line isn't a part of the list

    # print(word_to_index)
    return (word_list, word_to_index)

def compare_normal_to_reddit():
    reddit_words, reddit_occurences = get_scraped_sorted_words()
    english_words, english_occurences = get_english_common_words()

    difference_list = []
    for word in english_words:
        if word in reddit_words:
            # print(word)
            current_reddit_word_rank = len(reddit_words) - reddit_words.index(word)
            current_english_word_rank = english_occurences[word]
            # difference = abs(current_english_word_rank - current_reddit_word_rank)
            # print(current_english_word_rank, current_reddit_word_rank, word)
            difference_list.append((word, current_reddit_word_rank, current_english_word_rank))

    difference_list = sorted(difference_list, key = lambda element: abs(int(element[1] - element[2])))
    print("yes")
    for k in difference_list: print(abs(k[1] - k[2]), *k)
if __name__ == '__main__':
    # print(get_scraped_sorted_words())
    # get_english_common_words()

    compare_normal_to_reddit()

    # print(convert_all_memes_to_text(os.path.join("scraping", "auto_download1"),
    #                                 os.path.join("scraping", "exports")))

