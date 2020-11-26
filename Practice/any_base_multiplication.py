num1=int(input())
num2=int(input())
base=int(input())


def multiply_num1_with_num2(num1,multiplier,base):
    carry=0
    sum=0
    product=1
    while(num1 or carry):
       to_multiply_with=num1%10
       num1=num1//10
       
       remain=((to_multiply_with*multiplier)+carry)%base
       carry=((to_multiply_with*multiplier)+carry)//base
       sum+=remain*product
       product*=10
    return sum

def multiply_any_base(num1,num2,base):
    sum=0
    product=1
    while(num2):
            remain=num2%10
            num2//=10
            product_of_one=multiply_num1_with_num2(num1,remain,base)
            sum=addition_of_two_numbers(product_of_one*product,sum,base)
            product*=10
    return sum
            
def addition_of_two_numbers(num1,num2,base):
    carry=0
    product=1
    sum=0
    while(num1 or num2 or carry):
        remainder_1=num1%10
        remainder_2=num2%10
        remaider_3=(remainder_1+remainder_2+carry)%base
        carry=(remainder_1+remainder_2)//base
        sum+=remaider_3*product
        product*=10
        num1//=10
        num2//=10
    return sum

result=multiply_any_base(num1,num2,base)
print(result)

        



