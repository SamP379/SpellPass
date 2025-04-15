import os
import json
import word_utils


WORDS_FILE_PATH = "words.json"


def adjust_words(words : dict, amount : int) -> dict:
    """Adjusts a dictionary of words to be of length 'amount'"""
    difference = abs(len(words) - amount)
    if len(words) < amount:
        for i in range(difference):
            new_word = word_utils.get_random_word()
            words[new_word] = 0
    else:
        words_list = list(words)
        for i in range(difference):
            words.pop(words_list[i])
    return words


def load_words(amount : int) -> dict|None:
    try:
        with open(WORDS_FILE_PATH, mode = "r") as file:
            words = json.load(file)
            if len(words) != amount:
                words = adjust_words(words, amount)
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