# 4 -> input
# A
# BB
# CCC
# DDDD

num=int(input())

i=0
alpha=65
while i<num:
    j=0
    while j<=i:
        print(chr(alpha),end="")
        j+=1
    i+=1
    alpha+=1
    print()
    
        