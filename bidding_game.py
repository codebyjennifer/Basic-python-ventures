logo = """               ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\""""
print(logo)
more_bidders = True
dictionary = {}
while more_bidders:
    user_name = input("What is your name?: ")
    bid = int(input("What is your bid?: Rs"))
    dictionary[user_name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes or 'no'.")
    if other_bidders == "yes":
        print("\n" * 75)
    else:
        winner = ""
        highest_bid = 0
        for each_item in dictionary:
            bid_amount = dictionary[each_item]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = each_item
        more_bidders = False
        print(f'The winner is {winner} with a bid of Rs{highest_bid}!')
