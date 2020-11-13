# heads or tails
import random
num=int(input("Enter the seed: "))
random.seed(321)
random_int=random.randint(0,1)
print(random_int)
if random_int==1:
    print("Head")
else:
    print("Tail")


