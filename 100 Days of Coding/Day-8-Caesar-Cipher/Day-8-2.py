

# def check_prime(number):
#     for index in range(2,number):
#         if (number%index)==0:
#           print("This number is not a prime")
#           exit()
#     print("This is a prime number")
          

def check_prime(number):
    isprime=0
    for index in range(2,number):
        if (number%index)==0:
            isprime=1T
            
    if (isprime==0):
        print("This number is  a prime number")
    else:
          print("This number is not a prime")
          exit()
    print("This is a prime number")
          
num=int(input("Enter a number to check if it is a prime or not: "))

check_prime(num)
