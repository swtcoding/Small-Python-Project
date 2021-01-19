import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_num:
            print("It is too low.")
        elif guess > random_num:
            print("It is too high.")
    
    print(f"Congratulations! You have nailed it. The number is exactly {random_num}!")

guess(100)