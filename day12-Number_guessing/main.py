import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)

def difficulty_selection():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
attempts = difficulty_selection()
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < random_number:
        print("Too low.")
    elif guess > random_number:
        print("Too high.")
    else:
        print(f"You got it! The answer was {random_number}.")
        break
    attempts -= 1
    if attempts == 0:
        print(f"You have run out of attempts! The correct answer was {random_number}.")