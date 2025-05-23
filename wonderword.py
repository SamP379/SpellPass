import os
import word_utils
import storage_utils


class WonderWord:
    """A class to represent a WonderWord session. A WonderWord is a game 
    where the user can practise their spelling and vocab"""

    WORDS_FILE_PATH = "words.json"

    def __init__(self, words_amount : int):
        self.words_amount = words_amount
        self.words = self.get_words()
    

    def clear_screen(self):
        os.system("cls")
        

    def get_words(self) -> dict:
        """Loads the words from storage if they already exist or gets new words if they don't"""
        if os.path.exists(WonderWord.WORDS_FILE_PATH):
            words = storage_utils.load_words(self.words_amount)
            return words
        else:
            words = word_utils.get_random_words(self.words_amount)
            return words
    

    def display_word(self, word : str):
        """Displays the current practise word and uses text-to-speech to pronounce it"""
        self.clear_screen()
        print(word.title())
        word_utils.pronounce(word)
        self.clear_screen()


    def handle_guess(self, word : str):
        """Handles allowing the user to practise spelling the current word"""
        user_guess = input("Enter word: ").strip().lower()
        user_definition = input("Enter definition: ")
        if user_guess == word:
            self.words[word] += 1


    def handle_results(self, word : str):
        """Handles displaying the current practise word and it's definition"""
        print(f"\nWord: {word.title()}")
        word_definition = word_utils.get_definition(word)
        if word_definition is not None:
            print(f"Definition: {word_definition}")
        input("\nPress enter to continue ")


    def main_loop(self):
        """The main loop of the WonderWord program"""
        for word in self.words:
            self.display_word(word)
            self.handle_guess(word)
            self.handle_results(word)
        storage_utils.save_words(self.words)   