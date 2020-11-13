num=int(input())
i=0

while i<num:
    j=0
    while j<num:
        print(chr(ord('A')+(i+j)),end="")
        j=j+1
    print()
    i=i+1