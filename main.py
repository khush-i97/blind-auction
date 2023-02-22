#this code was compiled on replit
from replit import clear

bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amt = bidding_record[bidder]
    if bid_amt > highest_bid:
      highest_bid = bid_amt
      winner = bidder
  print(f"The winner of this bid is {winner} with a price of Rs {highest_bid}")

while not bidding_finished:
  name = input("Please provide us with your name: ")
  price = int(input("How much is your bid? Rs: "))
  bids[name] = price
  should_continue = input("Are there any other bidders present? Type 'yes' or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    clear()
    highest_bidder(bids)
  elif should_continue == "yes":
    clear()
