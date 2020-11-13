# tip calculator
print("Welcome to the tip calculator:")
total_bill= float(input("What was the total bill: $ "))
percentage_in_number=int(input("What perce           ntage tip would you like to give? 10,12 or 15? $ "))
split_people=int(input("How many people to split the bill? "))

percentage_tip=(percentage_in_number/100)*total_bill

share_per_head=(float((total_bill+percentage_tip)/split_people))
share_perhead=round(share_per_head,2) 

to_pay=print(f"Each person should pay: ${share_perhead}")



