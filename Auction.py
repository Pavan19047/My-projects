import os
from hammer import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
bids = {}

bidding_finished = False

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with bid amount of {highest_bid}")
while not bidding_finished:
  name = input("What is your name? ")
  bid_price = int(input("What's your bid price $"))
  bids[name] = bid_price
  should_cont = input("Are there any other bidders? ").lower()
  if should_cont == "no":
    bidding_finished = True
    highest_bidder(bidding_record=bids)
  elif should_cont == "yes":
    os.system('cls')
    
  








  
  