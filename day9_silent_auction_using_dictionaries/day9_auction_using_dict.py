from logos import bidding_logo
# Silent Auction using Dictionary, For Loops and While Loop

print(bidding_logo)

my_dict = {}

user_input_name = input("Whats your name: ")
user_input_price = round(float(input("Whats your bid: $ ")), 3)

my_dict[user_input_name] = user_input_price

user_on = input("Are there any more bidders? y or n ").lower()

while user_on == 'y':
    print("\n" * 100)  # since new coders don't know clear func for Pycharm Console
    user_input_name = input("Whats your name: ")
    user_input_price = round(float(input("Whats your $: ")), 3)
    my_dict[user_input_name] = user_input_price
    user_on = input("Are there any more bidders? y or n ").lower()

winner_name = ""
winner_bid = 0

for k,v in my_dict.items():
    if v > winner_bid:
        winner_name = k
        winner_bid = v

print(f"The winner of this silent auction is {winner_name} and the bid was ${winner_bid}")