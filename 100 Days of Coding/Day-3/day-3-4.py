# Pizza Billing System
pizza_size=input("Enter your pizza size: S, M or L ")
pizza_pepperoni=input("Do you want peppperoni: Y or N ")
pizza_cheeze=input("Do you want extra cheeze? Y or N ")

bill=0
if pizza_size=='S':
     bill=15
elif pizza_size=='M':
    bill=20
else:
    bill=25

if pizza_pepperoni=='Y':
    if pizza_size=='S':
        bill+=2
    else:
        bill+=3
if pizza_cheeze=='Y':
    bill+=1

print(f"Your final Bill is: ${bill}")




