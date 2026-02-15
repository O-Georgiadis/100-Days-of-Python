
all_bids = {}

def winner():
    highest_bid = 0
    winner_name = ""
    for name, amount in all_bids.items():
        if amount > highest_bid:
            highest_bid = amount
            winner_name = name
    print(f"The winner is {winner_name} with a bid of ${highest_bid}.")


print("Welcome to the secret auction program.")

bid_ends = False

while not bid_ends:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    all_bids[name] = bid
    more_bidders = input("Are there any other bidders? type 'yes' or 'no'.\n").lower()

    if more_bidders == 'yes':
        print("\n" * 40)
    else:
        winner()
        bid_ends = True


