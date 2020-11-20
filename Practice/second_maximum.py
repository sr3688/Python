
# x=[1,2,3,6,4,5,6,7]
# length=len(x)
# for index in range(0,length):
#     print(x[length-1],end=" ")
#     length-=1
# print()
    
numbers=input("Enter three numbers separated by a space: ").split()
a=int(numbers[0])
b=int(numbers[1])
c=int(numbers[2])

if a>b and a>c:
        if c>b:
             print(f"{c} is the second largest number")
        else:
             print(f"{b} is the second largest number")
elif b>c:
        if a>c:
              print(f"{a} is the second largest number")
        else:
              print(f"{c} is the second largest number")
else:
        if a>b:
              print(f"{a} is the second largest number")
        else:
              print(f"{b} is the second largest number")
    

        

