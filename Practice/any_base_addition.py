num1=int(input())
num2=int(input())
base=int(input())

carry=0
sum=0
product=1
while(num1 or num2 or carry):
    remainder_1=num1%10
    remainder_2=num2%10
    remaider_3=(remainder_1+remainder_2+carry)%base
    carry=(remainder_1+remainder_2)//base
    sum+=remaider_3*product
    product*=10
    num1//=10
    num2//=10

print(sum)