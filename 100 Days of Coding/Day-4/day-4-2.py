#random bill payer
import random
seed=int(input("Create a seed number: "))
random.seed(seed)

everybodysname=input("give me everybody's name,separated by a comma: ")

names=everybodysname.split(",")
print(names)
print(len(names))


bill_payer=names[random.randint(0,len(names)-1)]

print(f"{bill_payer} is going to buy the meal today")

