
def string_reverse(string):
    rev=""
    length=len(string)
    for index in range(len(string)):
        rev+= string[length-1]
        length-=1
    return rev
