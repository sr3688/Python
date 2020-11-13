print('''Welcome to the tresure island.
Your mission is to find the tresure.
''')
first_option=input("""You are at a cross road.Where do you want to go? "left" or "right": """)
if first_option=="left":
    print("Game over")
else:
    second_option=input("""You come to a lake.There is an island in the middle of the lake.Type "wait" to wait for a boat.Type "swim" to swim accross: """)
    if second_option=="swim":
        print("Game Over")
    elif second_option=="wait":
        third_option=input("You arrived at the island unharmed.There is a house with three doors. One red,one yellow and one blue. Which color do you choose? ")
        
        if third_option==("red" or "blue") :
            print("Game Over")
        elif third_option=="yellow":
            print("you win")

