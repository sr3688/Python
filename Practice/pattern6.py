# 1 23 456 78910

n=int(input())
i=1
num=1

while i<=n:
    j=1
    while j<=i:
        print(num,end="")
        num=num+1
        j=j+1
    print(end=" ")
    i=i+1
print()
    