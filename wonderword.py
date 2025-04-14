import os
import time
import word_utils



class WonderWord:

    WORDS_FILE_PATH = "words.csv"

    def __init__(self):
        self.words = self.get_words()
    

    def get_words(self):
        if os.path.exists(WonderWord.WORDS_FILE_PATH):
            pass
        else:
            words = word_utils.get_random_words(amount = 10)
            return words
    

    def clear_screen(self):
        os.system("cls")
        
    
    def main_loop(self):

        self.clear_screen()
        for word in self.words:
            print(word)
            time.sleep(4)
            self.clear_screen()
            user_guess = input("\nEnter word: ").strip().lower()
            user_definition = input("Enter definition: ")
            print(f"\nWord: {word}")
            word_definition = word_utils.get_definition(word)
            if word_definition is not None:
                print(f"Word definition: {word_definition}")
            input("")
            self.clear_screen()