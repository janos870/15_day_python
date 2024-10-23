import random
from art import logo


def deal_card():
    cards = [
                (11, "A"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"),
                (8, "8"), (9, "9"), (10, "10"), (10, "J"), (10, "Q"), (10, "K")
            ] * 4  # 4 color representation
    card = random.choice(cards)
    return card[0]


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(p_score, d_score):
    if p_score == d_score:
        return "Draw 🙃"
    elif d_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif p_score == 0:
        return "Win whit a Blackjack 😎"
    elif p_score > 21:
        return "Player went over, player lose 😭"
    elif d_score > 21:
        return "Opponent went over, player win 😁"
    elif p_score > d_score:
        return "Player win 😊"
    else:
        return "Player lose 😭"


def play_game():
    print(logo)
    player_hand = []
    dealer_hand = []
    player_score = -1
    dealer_score = -1
    is_game_over = False

    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        print(f"Your hand: {player_hand}, current score: {player_score}")
        print(f"Dealer's first hand: {dealer_hand[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            player_should_deal = input("type 'y' to hit, type 'n' to stand: ")
            if player_should_deal == "y":
                player_hand.append(dealer_hand)
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"Player final hand: {player_hand}, final score: {player_score} ")
    print(f"Dealer final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))


game_play = True

while game_play:
    player_choice = input("Do you want to play game Blackjack? Type 'y' or 'n': ")
    if player_choice == "y":
        print("\n" * 20)
        play_game()
    else:
        game_play = False
        print("\n" * 4)
        print("See you next time 🫱")
