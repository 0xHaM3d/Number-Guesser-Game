# Number Guesser Game

A simple, modular Python console application where the player tries to guess a randomly generated number between 1 and 100. The game provides hints and tracks your score based on the number of attempts.

## 🎮 Features

- Input Validation: Ensures the user enters a valid integer within the 1–100 range.

- Dynamic Hints: Provides feedback on whether your guess is too high or too low.

- Scoring System: Start with 100 points; lose 10 points for every incorrect guess.

## 📂 Project Structure

Based on the imports in `main.py`, your project should be organized like this:

```plaintext
num_guesser/
├── src/
│   ├── main.py                # Entry point of the game
│   ├── game_logic/
│   │   ├── number_generator.py # Generates the secret number
│   │   └── hint_generator.py   # Processes high/low hints
│   └── utils/
│       └── input_validator.py  # Handles user input and errors
└── README.md
```

## 🚀 How to Run

To avoid the `ModuleNotFoundError` and ensure Python recognizes the internal packages, run the game from the **root directory** (`num_guesser/`) using the module flag:
```Bash
python3 src/main.py
```

## 🕹️ How to Play

1. The game picks a secret number between 1 and 100.
2. Enter your guess when prompted.

3. If you are wrong, a hint will tell you if the number is higher or lower.

4. Each wrong guess reduces your score by 10 points (minimum score is 0).

5. The game ends when you guess the correct number!
