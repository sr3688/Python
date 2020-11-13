number=int(input("Enter a number to be reversed: "))

   
#234
rev=0

while number>0:
    num=number%10
    
    rev=(rev*10)+num
    number=number//10
print(rev) 
