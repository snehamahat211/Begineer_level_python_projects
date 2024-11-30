from asci import logoauction
import os

bidding_finished = False
newbid={}

def highest_bid(biddingrecords):
    highest_bid = 0
    winner=""

    for bidder in biddingrecords:
          bid_amount=biddingrecords[bidder]
          if bid_amount>highest_bid:
               highest_bid = bid_amount
               winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
while not bidding_finished:
# ask name and price of the bidder
    name=input("what is your name?")
    price=int(input("what is the amount you want to bid?"))
    newbid[name]=price
    should_continue=input("Is there any other bidder than you? .if yes type'yes'else 'no'")
    if should_continue=="no":
        bidding_finished=True
        highest_bid(newbid)
    elif should_continue=="yes":
        os.system('cls')

