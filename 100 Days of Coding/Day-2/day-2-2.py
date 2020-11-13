#BMI Calculator
weight=int(input("Enter your weight (kg): "))
height=float(input("Enter your Height (m): "))
BMI= weight/(height**2)
# print(format(BMI,'.2f'))
print(int(BMI))