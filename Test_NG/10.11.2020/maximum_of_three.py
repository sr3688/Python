import string
# def max_of_three(x,y,z):
#     return max_of_two(max_of_two(x,y),z)
    

# def max_of_two(x,y):
#     if x>y:
#         return x
#     return y



# print(max_of_three(1,2,-3))
numbers=input("Enter three numbers separated by space: ")
numbers_list=numbers.split(" ")
a=int(numbers_list[0])
b=int(numbers_list[1])
c=int(numbers_list[2])
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)