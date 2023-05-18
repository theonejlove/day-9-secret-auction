from replit import clear
from art import logo

print(logo)

bidding_info = {}


should_continue = True
while should_continue:
  name = input("What is your name?\n")
  bid = input("What's your bid?\n")
  bidding_info[name] = bid

  cont = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  clear()
  
  if cont == "no":
    should_continue = False
    highest_bid = 0
    winner = ""
    for bidder in bidding_info:
      price = int(bidding_info[bidder])
      if price >= highest_bid:
        highest_bid = price
        winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
