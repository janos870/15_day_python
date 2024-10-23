from game_data import data
from art import logo, vs
import random

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name} a {account_description} from {account_country}"


def check_answer(guesses, a_followers, b_followers):
    if a_followers > b_followers:
        return guesses == "a"
    else:
        return guesses == "b"


score = 0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more follower? Type A or B: ").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"Yore right current score is {score}")
    else:
        print(f"Sorry, that's wrong, final score: {score} ")
        game_should_continue = False


