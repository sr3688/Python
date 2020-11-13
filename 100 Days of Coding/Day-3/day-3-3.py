year=int(input("Enter the year to check if it a leap year: "))

# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("Leap Year.")
#         else:
#             print("Not leap")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year.")

if year%4==0:
    if year%100==0 and year%400==0:
        print("Leap Year")
    else:
        print("Not Leap Year")
else:
    print("Not Leap")