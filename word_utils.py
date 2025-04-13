import requests

DICTIONARY_ENDPOINT = "https://api.dictionaryapi.dev/api/v2/entries/en/"

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