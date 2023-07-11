import random
from JackArt import logo
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    
    if sum(cards) == 21 and len(cards) == 2:   #Black Jack condition
        return 0
    if 11 in cards and sum(cards) > 21:        #if ace in cards when sum > 21
        cards.remove(11)                       #remove 11
        cards.append(1)                        #and replace ace value as 1
        
    return sum(cards)  

def compare(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if computer_score == user_score:
        return "Draw 😒"
    elif computer_score == 0:
        return "You lose 😤, Opponent has Blackjack"
    elif user_score == 0:
        return "You win 😎 with a Blackjack"
    elif user_score > 21:
        return "You lose 😤"
    elif computer_score > 21:
        return "You win 😎"
    elif user_score > computer_score:
        return "You win 😎"
    elif computer_score > user_score:
        return "You lose 😤"

def play_game():
    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())               #gives two random cards to user
        computer_cards.append(deal_card())           #gives two random cards to computer

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} and current score = {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            
            user_deal = input("Type y to get another card and n to pass: ")
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('cls')
  play_game()
  
  