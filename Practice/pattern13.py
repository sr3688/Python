num=int(input())

i=0
while i<num:
    j=0
    while j<=i:
        if j==0 or j==i:
            print(1,end="")
        else:
            print(2,end="")
        j+=1
    i+=1
    print()