import os
import json
import word_utils


WORDS_FILE_PATH = "words.json"


def get_word():
    import random
    words = ("revolver", "gun", "rifle", "eastwood", "horse", "ranch", "books")
    return random.choice(words)


def adjust_words(words : dict, words_amount : int) -> dict:
    difference = abs(len(words) - words_amount)
    if len(words) < words_amount:
        for i in range(difference):
            new_word = word_utils.get_word() # TODO Implement get_word()
            words[new_word] = 0
    else:
        words_list = list(words)
        for i in range(difference):
            words.pop(words_list[i])
    return words


def load_words(words_amount : int) -> dict|None:
    try:
        with open(WORDS_FILE_PATH, mode = "r") as file:
            words = json.load(file)
            if len(words) != words_amount:
                words = adjust_words(words, words_amount)
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