import os
import word_utils
import storage_utils


class WonderWord:

    WORDS_FILE_PATH = "words.json"

    def __init__(self, words_amount : int):
        self.words_amount = words_amount
        self.words = self.get_words()
        

    def get_words(self) -> dict:
        if os.path.exists(WonderWord.WORDS_FILE_PATH):
            words = storage_utils.load_words()
            return words
        else:
            words = word_utils.get_random_words(self.words_amount)
            return words
    

    def clear_screen(self):
        os.system("cls")

    
    def display_word(self, word : str):
        self.clear_screen()
        print(word.title())
        word_utils.pronounce(word)
        self.clear_screen()


    def handle_guess(self, word : str):
        user_guess = input("Enter word: ").strip().lower()
        user_definition = input("Enter definition: ")
        if user_guess == word:
            self.words[word] += 1


    def handle_results(self, word : str):
        print(f"\nWord: {word.title()}")
        word_definition = word_utils.get_definition(word)
        if word_definition is not None:
            print(f"Definition: {word_definition}")
        input("\nPress enter to continue ")


    def main_loop(self):
        for word in self.words:
            self.display_word(word)
            self.handle_guess(word)
            self.handle_results(word)