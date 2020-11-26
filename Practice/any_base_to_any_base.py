num=int(input())
which_base_from=int(input())
which_base_to=int(input())


def any_base_to_any_base(num,which_base_from,which_base_to):
    sum_to_decimal=0
    sum_to_base_to=0
    product_to_decimal=1
    product_to_base_to=1
    while(num>0):
        remainder=num%10
        sum_to_decimal+=remainder*product_to_decimal
        product_to_decimal*=which_base_from
        num//=10
    while(sum_to_decimal):
        remainder=sum_to_decimal%which_base_to
        sum_to_base_to+=remainder*product_to_base_to
        product_to_base_to*=10
        sum_to_decimal//=which_base_to

    return sum_to_base_to

    
print(any_base_to_any_base(num,which_base_from,which_base_to))