import math 
height=float(input("Enter your height (m): "))
weight=float(input("enter your weight(kg): "))

BMI1=weight/(height*height)
BMI=math.ceil(BMI1)

if BMI<18.5:
    print(f"Your BMI is {BMI}, you are slightly Underweight")
elif BMI>18.5 and BMI<25:
    print(f"Your BMI is {BMI}, you are slightly Normal Weight")
elif BMI>25 and BMI<30:
    print(f"Your BMI is {BMI}, you are slightly Slightly Overweight")
elif BMI>30 and BMI<35:
    print(f"Your BMI is {BMI}, you are slightly Obese")
else:
    print(f"Your BMI is {BMI}, you are slightly Clinically Obese")


