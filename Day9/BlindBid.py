bids={}
Continue_Bidding=True

while Continue_Bidding:
    name=input("What is your name?: ")
    price=int(input("What is your bid?: $"))
    bids[name]=price
    should_continue=input("Are there any other bidders? Type 'yes' or 'no' .\n")
    if should_continue=="no":
        Continue_Bidding=False
        print("\n"*20)
        find_highest_bidder(bids)
    elif should_continue=="yes":
        print("\n"*20)
    

    def find_highest_bidder(Bidding_Dictionary):
        highest_bidder=""
        highest_bid=0
        for bidder in Bidding_Dictionary:
            Bid_Amount=Bidding_Dictionary[bidder]
            if(Bid_Amount>highest_bid):
                highest_bid=Bid_Amount
                highest_bidder=bidder

        print(f"The highest Bidder is {highest_bidder} and the bidding amount is ${highest_bid}")