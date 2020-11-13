# 4 ->input
# A
# AB
# ABC
# ABCD

num=int(input())
i=0
while i<num:
    j=0
    alpha=65
    while j<=i:
        print(chr(alpha),end="")
        alpha+=1
        j+=1
    i+=1
    print()