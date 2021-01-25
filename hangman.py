import random
from words import words

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
        user_letters = input("Guess a word:")
        if user_letters in alphabet - used_letters:
            used_letters.append(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)


