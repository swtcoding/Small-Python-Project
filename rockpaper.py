import random

def play():
    user = input("What will you choose? 'r' for rock, 'p' for paper, 's' for scissor\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return "It\'s a tie!"

    if win(user, computer):
        return "You won!"

    return "You lost!"

def win(user, computer):

    if (user == "r" and computer == "s") or (user =="s" and computer == "p") or (user == "p" and computer == "r"):
        return True

print(play())
