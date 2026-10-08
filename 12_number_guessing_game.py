# Number Guessing Game
import random

secret = random.randint(1, 10)
attempts = 0

print("I'm thinking of a number between 1 and 10.")

while True:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1
    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print(f"Correct! You found it in {attempts} attempt(s).")
        break
