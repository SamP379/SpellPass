import pyttsx3
import requests
import ai_utils
import wonderwords 


MAX_DEFINITION_LENGTH = 13
WONDERWORD = wonderwords.RandomWord()
DICTIONARY_ENDPOINT = "https://api.dictionaryapi.dev/api/v2/entries/en/"
LLAMA_DEFINITION_PROMPT = """Shorten this definition so that it's less than 13 words, 
                           and do not give any other kind of text except the definition: """


def pronounce(word : str):
    """Uses pyttsx3 text-to-speech to pronounce a given word"""
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()


def get_random_word() -> str:
    """Returns a random word"""
    random_word = WONDERWORD.word(word_min_length = 3, word_max_length = 14)
    return random_word


def get_random_words(amount : int) -> dict:
    """Returns a dictionary of random words."""
    random_words = WONDERWORD.random_words(amount, word_min_length = 3, word_max_length = 14)
    words = {}
    for word in random_words:
        words[word] = 0
    return words


def sanitize_definition(word_definition : str) -> str:
    """Sanitizes the definition of a word"""
    if len(word_definition.split()) > MAX_DEFINITION_LENGTH:
        llama_prompt = LLAMA_DEFINITION_PROMPT + word_definition
        short_definition = ai_utils.get_llama_response(llama_prompt) 
        if short_definition is not None:
            return short_definition
    return word_definition


def get_definition(word : str) -> str|None:
    """Returns the definition of a given word"""
    try:
        endpoint = DICTIONARY_ENDPOINT + word
        response = requests.get(url = endpoint)
        definition = response.json()[0]["meanings"][0]["definitions"][0]["definition"]
        definition = sanitize_definition(definition)
        return definition
    except Exception as error:
        print(f"An error occured: {error}")
        return None