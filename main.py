from random import randint


def setup_difficulty():
    """Asks the user for a difficulty level and returns the game settings."""
    while True:
        user_choice = input("Choose difficulty (easy, medium, hard): ").lower()
        if user_choice in ['hard', 'medium', 'easy']:
            break
        else:
            print("Invalid input! Please choose again.")

    if user_choice == 'easy':
        return 50, 10  # max_number, guess_limit
    elif user_choice == 'medium':
        return 100, 7
    else:  # 'hard'
        return 200, 5

def play_game(max_number, guess_limit):
    """Runs a single round of the Guess the Number game."""
    secret_number = randint(1, max_number)
    number_of_guesses = 0
    user_guess = None  # Initialize user_guess to handle edge cases

    print(f"\nI've chosen a number between 1 and {max_number}. You have {guess_limit} tries.")

    while number_of_guesses < guess_limit:
        try:
            user_guess = int(input(f"Guess #{number_of_guesses + 1}: "))
        except ValueError:
            print("That's not a number! Please enter only a number.")
            continue

        number_of_guesses += 1
        if user_guess > secret_number:
            print("Too high!")
        elif user_guess < secret_number:
            print("Too low!")
        else:
            print(f"You guessed it right! It took you {number_of_guesses} guesses.")
            return  # Exit the function on a win

    # This part only runs if the loop finishes without a win
    print(f"\nGame over! You ran out of guesses. The secret number was {secret_number}.")

def ask_to_play_again():
    """Asks the user if they want to play again and returns a boolean."""
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "no"]:
            return play_again == 'yes' # Returns True if 'yes', False if 'no'
        else:
            print("Invalid input!")

def main():
    """The main function to orchestrate the game."""
    print("--- Welcome to the Guess the Number Game! ---")
    while True:
        # 1. Get settings for the new game
        max_number, guess_limit = setup_difficulty()

        # 2. Play one round of the game with those settings
        play_game(max_number, guess_limit)

        # 3. Ask the user if they want to continue
        if not ask_to_play_again():
            print("Thanks for playing!")
            break

# This is the standard entry point for a Python script
if __name__ == "__main__":
    main()
