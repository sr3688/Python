# 5 -> input
#     1
#    121
#   12321
#  1234321
# 123454321

num=int(input())

i=1
space=num-i
number=1

while i<=num:
    j=1
    counting=1
    while j<=space:
        print(" ",end=" ")
        j+=1
   
    j=1
    while j<=number:
        print(counting,end="")
        
        if j<=(number//2):
            counting+=1
        else:
            counting-=1
        j+=1
    space-=1
    number+=2
    i+=1
    print()
        


