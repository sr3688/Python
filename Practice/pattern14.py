# 10 -> input
# 12345678910
# 123456789
# 12345678
# 1234567
# 123456
# 12345
# 1234
# 123
# 12
# 1

num=int(input())

i=0
while i<num:
    j=1
    while j<=num-i:
        print(j,end="")
        j+=1
    i+=1
    print()
    