import random



def card_deal():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card


def compare(user_count, computer_count):
    if user_count == computer_count:
        return "It's a draw!"
    elif user_count == 0:
        return "Blackjack! You win!"
    elif computer_count == 0:
        return "Computer has Blackjack! You lose!"
    elif user_count > 21:
        return "You went over 21. You lose!"
    elif computer_count > 21:
        return "Computer went over 21. You win!"
    elif user_count > computer_count:
        return "You win!"
    elif user_count < computer_count:
        return "You lose!"
    else:
        return "Error in comparison!"

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)



def play_game():
    game_over = False
        
    computer_hand = []
    user_hand = []
    for _ in range(2):
        user_hand.append(card_deal())
        computer_hand.append(card_deal())
        

    while not game_over:    
        user_count = calculate_score(user_hand)
        computer_count = calculate_score(computer_hand)

        print(f"Your cards are: [{user_hand}] , current score: {user_count}")
        print(f"Computer's first card: [{computer_hand[0]}]")

        if user_count == 0 or computer_count == 0 or user_count > 21:
            print(compare(user_count, computer_count))
            game_over = True
        else:
            continue_game = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if continue_game == "y":
                user_hand.append(card_deal())
            else:
                game_over = True           
        


    while computer_count != 0 and computer_count < 17:
        computer_hand.append(card_deal())
        computer_count = calculate_score(computer_hand)

    print(f"Your final hand: {user_hand}, final score: {user_count}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_count}")
    print(compare(user_count, computer_count))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")   == "y":
    print("\n" * 100)
    play_game() 