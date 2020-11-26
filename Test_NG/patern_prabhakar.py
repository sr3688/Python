     
# 1212
# 2121
# 1212
# 2121
num=int(input("Enter"))
i=1
column=2
while i<=num:
    j=1
    while j<=num:
        if i%2==1:
            if j%2==0:
                print(column,end="")
            else:
                print(column-1,end="")
        else:
            if j%2==0:
                print(column-1,end="")
            else:
                print(column,end="")
        j+=1

    i+=1
    print()



    
  




