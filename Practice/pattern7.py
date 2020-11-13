# ABCD ABCD ABCD ABCD

alpha1=int(input())
i=0
if alpha1<=26 and alpha1>=1:
        while i<alpha1:
            j=0
            while j<alpha1:
                print(chr(ord('A')+j),end="")
                j=j+1
            print()
            i=i+1
        print()
else:
    print("Please enetr the mumber between 1-26 ")
