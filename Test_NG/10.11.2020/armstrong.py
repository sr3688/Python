number=int(input())
length=len(str(number))
numcpy=number
sum=0
while numcpy:
       i=0
       product=1
       base= numcpy%10
    
       while i<length:
           product*=base 
           i+=1
       sum+=product
       numcpy//=10
if sum==number:
    print("This is an armstrong number")
else:
    print("Ths is not an armstrong number")
    

        
        
    
        
        