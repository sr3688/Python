number=int(input())
base=int(input())
multiply=1
sum=0
while(number>0):
    
    rem=number%10
    sum+=multiply*rem
    multiply*=base
    number//=10

print(sum)