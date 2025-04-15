import os
import json


WORDS_FILE_PATH = "words.json"


def load_words():
    try:
        with open(WORDS_FILE_PATH, mode = "r") as file:
            words = json.load(file)
            return words  
    except Exception as error:
        print(f"An error occured: {error}")
        return None


def remove_completed_words(words : dict) -> dict:
    for word in list(words):
        if words[word] >= 3:
            words.pop(word)
    return words


def save_words(words : dict):
    words = remove_completed_words(words)
    try:
        with open(WORDS_FILE_PATH, mode = "w") as file:
            json.dump(words, file, indent = 4)
    except Exception as error:
        print(f"An error occured: {error}")