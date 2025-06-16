# 🎲 Guess the Number Game

A classic "Guess the Number" command-line game written in Python. This project was built to practice fundamental programming concepts and has been enhanced with several features to create a complete, robust, and user-friendly experience.

It effectively demonstrates core skills such as loops, conditionals, user input validation, and error handling.

## ✨ Key Features

* **Dynamic Difficulty Levels:**
    * Choose between **Easy**, **Medium**, and **Hard** modes at the start of each game.
    * The number range and guess limits automatically adjust based on the chosen difficulty.

* **Robust Error Handling:**
    * The game gracefully handles non-numeric input for guesses using a `try-except` block, preventing crashes and prompting the user for a valid number without penalizing their turn count.

* **Comprehensive Input Validation:**
    * Ensures the user selects a valid difficulty level before the game starts.
    * Requires a clear "yes" or "no" response to play again, preventing ambiguity.

* **Replayability:**
    * After each game (win or lose), the user is given the option to play another round without restarting the script.

* **Interactive Feedback:**
    * Clear, real-time feedback tells the user if their guess is too high, too low, or correct.
    * At the end of a losing round, the secret number is revealed.

## 🚀 How to Run

1.  Ensure you have Python 3 installed on your system.
2.  Clone this repository or download the `game.py` file.
3.  Open your terminal and navigate to the project directory.
4.  Run the script with the following command:
    ```bash
    python game.py
    ```