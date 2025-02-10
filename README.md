# Wordle-Style Game

## Introduction
Welcome to the **Wrodle Game**! This is a simple word-guessing game inspired by Wordle, where players guess letters in a randomly selected five-letter word. The game provides feedback after each guess, helping the player figure out the correct word.

## How to Play
1. The game randomly selects a five-letter word from a word list.
2. You will guess one letter at a time for each position in the word.
3. The game will provide feedback on whether your guess is correct, incorrect, or present elsewhere in the word.
4. Continue guessing letters until you complete the full word.
5. The game will count the number of attempts you take to guess the full word.
6. Special messages appear based on your performance or specific words!

## Features
- Randomly selects a word from a word list file.
- Step-by-step letter guessing with feedback.
- Special Easter eggs for specific words and attempt counts.
- Keeps track of the number of guesses taken.

## Installation & Setup
1. Ensure you have Python installed on your system.
2. Prepare a text file containing a list of five-letter words (one per line) and save it Or feel free to use the provided worlist.
3. Update the file path in the script to point to your word list.
4. Run the script using Python:
   ```sh
   python wordle_game.py
   ```

## Easter Eggs
- Typing **"duck"** as a guess triggers a funny response.
- If the selected word is **"fatal"**, you'll get a humorous message.
- If you guess the word in **5 attempts**, the game acknowledges your skill.
- If you take **100 or more attempts**, the game humorously comments on your persistence!

## Future Improvements
- Add a graphical interface for better user experience.
- Implement a scoring system based on efficiency.
- Introduce difficulty levels with different word lengths.

Enjoy playing Wrodle and have fun guessing!

## License
This project is open-source and free to use. Feel free to modify and improve it!

