num=int(input())
base=int(input())
ten=1
sum=0
while(num):
    
    rem=num%base
    sum+=rem*ten
    ten*=10
    num=num//base
print(sum)   


    
        
    




    
        

