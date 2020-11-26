import os


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)    

bid={}
carryon=True
while(carryon):
    name=input("Please Enter Your Name: ")
    bid_price=int(input("Enter the bid price: "))

    bid[name]=bid_price

    more_bidders=input("Are there any more bidders? Yes or No? ").lower()

    if more_bidders=="no" or more_bidders=="n":
        carryon=False
    else:
        os.system('clear')


maximum=0
highest_bidder=""
for key in bid:
    if bid[key]>maximum:
        highest_bidder=""
        maximum=bid[key]
        highest_bidder=key

print(f"The higgest bid is {maximum} which is made by Mr.{highest_bidder}")
