import os
import time
import word_utils
import wonderwords 


def main():

    wonderword = wonderwords.RandomWord() 
    random_words = wonderword.random_words(amount = 10, word_min_length = 3, word_max_length = 14)

    os.system("cls")
    for word in random_words:
        print(word)
        time.sleep(5)
        os.system("cls")
        user_guess = input("\nEnter word: ").strip().lower()
        user_definition = input("Enter definition: ")
        print(f"\nWord: {word}")
        word_definition = word_utils.get_definition(word)
        if word_definition is not None:
            print(f"Word definition: {word_definition}")
        time.sleep(5)
        os.system("cls")



        

    
main()