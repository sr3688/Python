num1=int(input())
num2=int(input())
base=int(input())

carry=0
product=1
sum=0
while(num1 or num2 or carry):
    remain1=num1%10
    remain2=num2%10
    remain1+=carry
    if(remain1>=remain2):
        carry=0
        remain3=remain1-remain2
    else:
        carry=-1
        remain1+=base
        remain3=remain1-remain2
    sum+=remain3*product
    product*=10
    num1//=10
    num2//=10
print(sum)


