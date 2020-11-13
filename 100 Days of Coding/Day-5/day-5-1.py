# Average Height

# heights=input("Enter the Heights (in cm) separated by comma: ")

# height_list= heights.split(",")

# length_list=len(height_list)

# height_list_int=list(map(int,height_list))


# sum=0
# for height in height_list_int:
#     sum+=height

# average_height=sum/length_list
# print(f"The average height is {average_height}")

heights=input("Enter the Heights (in cm) separated by comma: ").split(",")

count=0
for num in heights:
    count+=1
sum=0
for n in heights:
    sum+=int(n)
    
print(round(sum/count))


