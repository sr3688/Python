#treasure placement
one=[" "," "," "]
two=[" "," "," "]
three=[" "," "," "]
four=[one,two,three]
print(f"1{one}\n\n2{two}\n\n3{three}\n \nWhere do you want to put the treasure: ",end=" ")
treasure_index=int(input())
print()
four[int(str(treasure_index)[1])-1][int(str(treasure_index)[0])-1]='X'
print(f"1{one}\n\n2{two}\n\n3{three}\n ")
