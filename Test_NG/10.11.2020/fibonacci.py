num=int(input())

counter=0
sum1=0
sum2=0

while counter<num:
    if counter==0:
        sum1+=0
        print(sum1,end=" ")
        counter+=1
    elif counter==1:
        sum2+=1
        print(sum2, end=" ")
        counter+=1
    else:
        fibonacci=0
        fibonacci+= sum1+sum2
        print(fibonacci,end=" ")
        temp=0
        sum1=sum2
        sum2=fibonacci
        counter+=1
print()
        
        
        
# num=int(input())

# counter=0
# sum1=0
# print(sum1,end=" ")
# sum2=1
# print(sum2,end=" ")
# while counter<num-2:
#         fibonacci=0
#         fibonacci+= sum1+sum2
#         print(fibonacci,end=" ")
#         temp=0
#         sum1=sum2
#         sum2=fibonacci
#         counter+=1
# print(sum2)

# num=int(input())

# counter=0
# sum1=1
# sum2=1

# while counter<num:
#         while counter<2:
#              print("1",end=" ")
#              counter+=1
#         fibonacci=0
#         fibonacci+= sum1+sum2
#         print(fibonacci,end=" ")
#         temp=0
#         sum1=sum2
#         sum2=fibonacci
#         counter+=1
# print()
        
        


        

        

