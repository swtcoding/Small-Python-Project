import random

def play():
    user = input("What will you choose? 'r' for rock, 'p' for paper, 's' for scissor ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return "It\'s a tie!"

    if win():
        return "You won!"

def win()

    if (user == "r" and computer == "s") or (user =="s" and computer == "p") or (user == "s" and computer == "p"):
        return True

return "You lost!"

print(play)
