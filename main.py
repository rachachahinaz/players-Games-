import game1
import game2
import players

def main():
    player_name = None
    while player_name is None:
        player_name = players.login()

    while True:
        print("\nChoose a game:")
        print("1. Hangman")
        print("2. Guess Number")
        choice = input("Enter the game number (or 'q' to quit): ")

        if choice == "1":
            game1_instance = game1.Game1()
            score = game1_instance.play_game()
        elif choice == "2":
            score = game2.play_game()
        elif choice.lower() == 'q':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice, please select 1 or 2.")
            continue


        players.update_score(player_name, score)

        play_again = input("Do you want to play another game? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
