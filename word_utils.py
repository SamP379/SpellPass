import pyttsx3
import requests
import wonderwords 

DICTIONARY_ENDPOINT = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def pronounce_word(word : str):
    """Uses pyttsx3 text-to-speech to pronounce a given word"""
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()


def get_random_words(amount : int) -> list:
    """Returns a list of random words."""
    wonderword = wonderwords.RandomWord() 
    random_words = wonderword.random_words(amount, word_min_length = 3, word_max_length = 14)
    return random_words


def get_definition(word : str):
    """Returns the definition of a given word or None if not found"""
    try:
        endpoint = DICTIONARY_ENDPOINT + word
        response = requests.get(url = endpoint)
        content = response.json()
        definition = content[0]["meanings"][0]["definitions"][0]["definition"]
        return definition
    except Exception as error:
        print(f"An error occured: {error}")
        return None