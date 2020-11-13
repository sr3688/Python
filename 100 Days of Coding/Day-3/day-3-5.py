# Love Calculator
import string
name1=input("EEnter Your name: ").lower()

name2=input("Enter the name of your partner: ").lower()

# count TRUE

T=name1.count('t')+name2.count('t')
R=name1.count('r')+name2.count('r')
U=name1.count('u')+name2.count('u')
E=name1.count('e')+name2.count('e')

total_true=T+R+U+E
#Count LOVE

L=name1.count('l')+name2.count('l')
O=name1.count('o')+name2.count('o')
V=name1.count('v')+name2.count('v')
E=name1.count('e')+name2.count('e')

total_love=L+O+V+E
love_calculate=int(str(total_true)+str(total_love))

if love_calculate<10 and love_calculate>90:
    print(f"Your score is {love_calculate},you go together like coke and mentos.")
elif love_calculate>40 and love_calculate<50:
    print(f"Your score is {love_calculate}, you are alright together.")
else:
    print(f"Your score is {love_calculate}.")




