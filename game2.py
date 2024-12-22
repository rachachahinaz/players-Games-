import random

def play_game():
    print("Game 2: Guess the Number between 50 and 100!")
    number = random.randint(50, 100)
    attempts = 5

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}/{attempts}. Guess the number: "))

        if guess == number:
            print("Congratulations!  woooow You guessed the correct number!")
            return 10
        elif guess < number:
            print("Too low! Try again pleas.")
        else:
            print("Too high! Try again pleas.")


    print(f"Sorry, you've used all {attempts} attempts. The correct number was {number}.")
    return 0
