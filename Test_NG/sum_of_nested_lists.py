# Sum of nested lists

def rec(list_a):
    sum=0
    
    for index in list_a:
        if type(index)==list:
            sum+=rec(index)
        else:
            sum+=index
    return sum
list_a=[1,[2,[3,5,[4]]],5,6,[10]]
print(rec(list_a))





