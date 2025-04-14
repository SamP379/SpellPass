import os
import time
import word_utils
import storage_utils


class WonderWord:

    WORDS_FILE_PATH = "words.json"

    def __init__(self, words_amount : int):
        self.words_amount = words_amount
        self.words = self.get_words()
        self.clear_screen()


    def get_words(self) -> dict:
        if os.path.exists(WonderWord.WORDS_FILE_PATH):
            words = storage_utils.load_words()
            return words
        else:
            words = word_utils.get_random_words(self.words_amount)
            return words
    

    def clear_screen(self):
        os.system("cls")


    def make_guess(self, word : str):
        self.user_guess = input("\nEnter word: ").strip().lower()
        user_definition = input("Enter definition: ")
        if self.user_guess == word:
            self.words[word] += 1


    def word_result(self, word : str):
        print(f"\nWord: {word.title()}")
        word_definition = word_utils.get_definition(word)
        if word_definition is not None:
            print(f"Definition: {word_definition}")
        input("\nPress enter to continue ")


    def main_loop(self):
        for word in self.words:
            print(word.title())
            word_utils.pronounce(word)
            self.clear_screen()
            self.handle_guess(word)
            self.word_result(word)
            self.clear_screen()