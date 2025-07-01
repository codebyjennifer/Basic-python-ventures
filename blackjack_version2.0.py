import random
import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""



restart = True
while restart:

    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if play_game == "y":
        print(logo)

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_cards = []
        computer_cards = []
        user_random_card = random.choices(cards, k=2)
        user_cards += user_random_card
        user_score = sum(user_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        computer_random_card = random.choices(cards, k=2)


        computer_cards += computer_random_card
        computer_score = sum(computer_cards)
        if computer_score <15:
            computer_cards += random.choice(cards)
        print(f"    Computer's first card: {computer_cards[0]}")
        new_card = True
        while new_card:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == "y" and user_score <21 and computer_score <21:

                add_card = random.choice(cards)
                user_cards.append(add_card)
                user_score += add_card
                print(f" Your cards: {user_cards}, current score: {user_score}\n Computer's first card: {computer_cards[0]}")
            else:

                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                if user_score <= 21 and user_score > computer_score:
                    print("Congratulations!! You won!")
                elif computer_score <= 21 and computer_score > user_score:
                    print("Computer won. Try again next time!")
                elif user_score > 21 and computer_score > 21:
                    print("You and computer went over! No one won! Try again!")
                elif user_score > 21:
                    print("You went over! Computer won.")
                elif computer_score > 21:
                    print("Computer went over! You won.")
                elif user_score == computer_score:
                    print("Draw! No one won. Try again next time")

                new_card = False





    else:
        restart = False






def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()








