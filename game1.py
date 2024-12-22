import random

class Game1:
    def __init__(self):
        self.word_groups = {
            "Countries": ["argentina", "brazil", "canada", "denmark", "egypt"],
            "Fruits": ["apple", "banana", "cherry", "grape"],
            "Technology": ["computer", "programming", "algorithm"],
            "familly": ["mather", "father","sister"],
            "Activities ": ["football", "travel","play guitar"],
            "Foods and Desserts": ["chocolate"],

        }

    def play_game(self):
        print("Game 1: Hangman")
        print("Choose a category:")
        categories = list(self.word_groups.keys())
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")

        chosen_index = int(input("Enter the number of the category pleas: ")) - 1

        if 0 <= chosen_index < len(categories):
            chosen_category = categories[chosen_index]
            word_to_guess = random.choice(self.word_groups[chosen_category])
            guessed_letters = []
            attempts = 8
            print(f"chose the category: {chosen_category}.")
            print(f"You have {attempts} attempts to guess the word.")

            while attempts > 0:
                current_guess = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
                print("Current word:", current_guess)

                guess = input("Guess a letter: ").strip().lower()

                if guess in guessed_letters:
                    print("You already guessed that letter !.")
                elif guess in word_to_guess:
                    guessed_letters.append(guess)
                    print("Good guess!")
                else:
                    guessed_letters.append(guess)
                    attempts -= 1
                    print("Wrong guess! Attempts left:", attempts)

                if all(letter in guessed_letters for letter in word_to_guess):
                    print(f"Congratulations! You guessed the word: {word_to_guess}")
                    return 10
            else:
                print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")
        else:
            print("Invalid category number.")
        return 0
