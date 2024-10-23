import random
from art import logo

print("Wellcome to the number guessing game 🙃")

game_difficulty_level = {
    "easy": 20,
    "medium": 15,
    "hard": 5
}


def display_difficulty_level():
    print("Available difficulty levels:")
    for level, attempts in game_difficulty_level.items():
        print(f"{level.capitalize()}: {attempts} attempts")

def set_difficulty():
    while True:
        game_difficulty = input("Please chose a game difficulty level Type: (easy, medium, hard): ")
        if game_difficulty in game_difficulty_level:
            return game_difficulty_level[game_difficulty]
        else:
            print("Invalid game difficulty level! Type: (easy, medium, hard)")


def start_game():
    print(logo)
    display_difficulty_level()
    max_attempts = set_difficulty()
    random_number = random.randint(0, 20)
    attempts = max_attempts

    while attempts > 0:
        guess_number = int(input(f"Guess a number (Remaining attempts: {attempts}): "))
        attempts -= 1

        if guess_number > random_number:
            print("The number is higher.")
        elif guess_number < random_number:
            print("The number is lower.")
        else:
            print(f"You guessed the number after {max_attempts - attempts} attempts 👏")
            break

        if attempts == 0:
            print(f"Out of attempts! The correct number was {random_number}. Better luck next time! 🙃")

    start_new_game()

def start_new_game():
    new_game = input("Would you like to play a new game? Type 'y' or 'n' ").lower()
    if new_game == "y":
        print("\n" * 20)
        start_game()
    else:
        print("\n" * 2)
        print("Goodbye ✌️")

start_game()








