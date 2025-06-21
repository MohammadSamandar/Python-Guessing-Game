# 🎲 Guess the Number Game

A classic "Guess the Number" command-line game written in Python. This project was initially a simple script and has been **refactored into a well-structured, function-based application** to demonstrate best practices in code organization, readability, and modular design.

It effectively showcases a solid understanding of fundamental Python concepts, from loops and conditionals to robust error handling and structured programming.

## ✨ Key Features

* **Dynamic Difficulty Levels:** Choose between **Easy**, **Medium**, and **Hard** modes, which automatically adjust the number range and guess limits.
* **Robust Error Handling:** The game gracefully handles non-numeric input for guesses using a `try-except` block, preventing crashes.
* **Comprehensive Input Validation:** Ensures the user selects a valid difficulty and a clear "yes" or "no" response for replaying.
* **Replayability:** A clean game loop allows the user to play multiple rounds without restarting the script.
* **Interactive Feedback:** Clear, real-time feedback tells the user if their guess is too high, too low, or correct.

## 🏗️ Code Structure

The application has been refactored into several distinct functions, each with a single, clear responsibility. This modular approach makes the code easier to read, maintain, and debug.

* `main()`: The primary function that orchestrates the overall game flow.
* `setup_difficulty()`: Handles user input for selecting a difficulty and returns the corresponding game settings (`max_number`, `guess_limit`).
* `play_game()`: Contains the core logic for a single round of the game, taking the difficulty settings as parameters.
* `ask_to_play_again()`: Manages the user prompt for replaying and returns a boolean value.

The script uses the `if __name__ == '__main__':` construct, making it a reusable module as well as a runnable program.

## 🚀 How to Run

1.  Ensure you have Python 3 installed on your system.
2.  Clone the repository or download the `game.py` file.
3.  Open your terminal and navigate to the project directory.
4.  Run the script with the following command:
    ```bash
    python game.py
    ```
