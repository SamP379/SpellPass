import requests
import wonderwords 

DICTIONARY_ENDPOINT = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def main():

    wonderword = wonderwords.RandomWord() 
    random_words = wonderword.random_words(amount = 10, word_min_length = 3, word_max_length = 14)

    try:
        endpoint = DICTIONARY_ENDPOINT + "saloon"
        response = requests.get(url = endpoint)
        content = response.json()
        definitions = content[0]["meanings"][0]["definitions"][0]["definition"]
        print(definitions)
    except Exception as error:
        print(f"An error occured: {error}")

    
main()