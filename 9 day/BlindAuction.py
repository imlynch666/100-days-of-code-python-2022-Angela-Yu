import art
import os


# def clear_console():
#     os.system('cls')
# clear_console()


print(art.logo)

print('Welcome to the auction')



#
# def auction():
#     all_data = []
#
#     name = input("What's your name: ")
#     bid = input("What's your bid: $")
#
#
#     def script_auction(name_s, bid_s, all_data_s):
#
#         new_data = {}
#         new_data[name_s] = bid_s
#         all_data_s.append(new_data)
#
#     script_auction(name, bid, all_data)
#
#     choice = input('Are there any others bidders? YES or NO: ').lower()
#     if choice == 'yes':
#         print("\n" * 99999)
#         auction()
#     elif choice == 'no':
#         print("\n" * 99999)
#
#         #didnt work correctly
#         print(all_data.sort(key=max))
#         print(all_data)
#     else:
#         print('Error')
#
#
# auction()



all_data = {}
biddingFinished = False

def script_auction(all_data_s):




while not biddingFinished:


    name = input("What's your name: ")
    bid = int(input("What's your bid: $"))

    all_data[name] = bid

    choice = input('Are there any others bidders? YES or NO: ').lower()

    if choice == 'no':
        biddingFinished = True
        script_auction(all_data)
    elif choice == 'yes':
        print(100*'*')







