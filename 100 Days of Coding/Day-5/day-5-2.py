#Highest Marks
marks=input("Enter the marks: ").split()

maximum=0
for mark in range(0,len(marks)):
    maximum=int(marks[0])
    if int(marks[mark])>maximum:
        maximum=marks[mark]
print(f"The highest score in the class is: {maximum}")

    
    

