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
    
    while len(word) > 0:
        user_word = input("Guess a word:")
        if user


