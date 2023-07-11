import random 
import os
from HLGame_data import data
from HLart import logo
from HLart import vs

def format(account):
    account_name = account["name"]
    followers = account["follower_count"]
    description = account["description"]
    country = account["country"]
    return f"{account_name}, a {description}, from {country} "

def check_answer(guess,a_followers,b_followers):
    
    if a_followers > b_followers:
       return guess == "a"
    else:
        return guess == "b"
    

score = 0
account_b = random.choice(data)

game_should_continue = True
while game_should_continue:
    print(logo)
    account_a = account_b
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format(account_a)}")
    print(vs)
    print(f"Compare B: {format(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_corect = check_answer(guess, a_follower_count, b_follower_count)

    if is_corect:
        score += 1
        print(f"You're Right!, Current Score: {score}")
        os.system('cls')
        
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
