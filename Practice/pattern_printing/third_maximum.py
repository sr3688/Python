import third_maximum_module
numbers=input("Enter the four numbers separated by space: ")
numbers_list=numbers.split(" ")
a=int(numbers_list[0])
b=int(numbers_list[1])
c=int(numbers_list[2])
d=int(numbers_list[3])

if a>b and a>c and a>d:
    third_maximum_module.maxium_of_three(b,c,d)
elif b>c and b>d and b>a:
    third_maximum_module.maxium_of_three(a,c,d)
elif c>d and c>a and c>b:
    third_maximum_module.maxium_of_three(a,b,d)
else:
    third_maximum_module.maxium_of_three(a,b,c)
    


    


    
   
    
