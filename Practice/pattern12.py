num=int(input())
i=0
while i<num:
    j=0
    while j<=i:
        if(i==0):
             print(1,end="")
             
        elif j==0 or j==i:
            print(i,end="")
           
        else:
            print(0,end="")
        j+=1
    i+=1
    print()
    

