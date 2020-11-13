age=int(input("Plaese enter your age: "))
remaining_age=90-age
days=remaining_age*365+(remaining_age//4)
weeks=days//7
months=days//30

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# print(f"You have {(90-age)*365+((90-age)//4)} days, {((90-age)*365+((90-age)//4))//7} weeks, and {((90-age)*365+((90-age)//4))//30} months left.")
