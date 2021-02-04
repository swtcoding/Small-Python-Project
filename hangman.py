import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    while len(word) > 0:

        print("You have gussed: " + " ".join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current words ", " ".join(word_list))

        user_letters = input("Guess a word: ")
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
        elif user_letters in used_letters:
            print("The character has been used. Try another one!")
        else:
            print("Invalid choice. Please try again.")

    print("Bingo! You have guessed the word!")

print(hangman())
