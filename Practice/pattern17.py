#  5 ->input
#      *
#     **
#    ***
#   ****
#  *****

# num=int(input())
# i=0
# while i<num:
#      j=0
    
#      while j<num:
#           if j<num-i-1:
#              print(" ",end="")
#              j+=1
#           else:
#              print("*",end="")
#              j+=1
#      i+=1
#      print()

num=int(input())
i=1
while i<=num:
         space=1
         while space<=num-i:
             print(" ",end="")
             space=space+1
         star=1
         while star<=i:
             print("*",end="")
             star+=1
         i+=1
         print()
     

# num=int(input())
# i=0
# while i<num:
#          j=0
#          while j<num-i-1:
#              print(" ",end="")
#              j+=1
#          j=0
#          while j<i+1:
#              print("*",end="")
#              j+=1
#          i+=1
#          print()
    
# num=int(input())
# i=0

# while i<num:
#          j=0
#          space=num-i-1
         
#          while j<space:
#              print(" ",end="")
#              j+=1
#          star=i+1
#          j=0
#          while j<star:
#              print("*",end="")
             
#              j+=1
#          i+=1
#          print()
            
            
