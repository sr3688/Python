number=int(input())

i=1
sum=0
while i<number:
    if number%i==0:
         sum+=i
    i+=1
if sum==number:
    print("This is a perfect number")
else:
    print("This is not a perfrct number")
    