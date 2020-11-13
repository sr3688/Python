#Rock Paper Scisor
import random

user=int(input("What do you choose? 0 for Rock, 1 for Paper, 2 scissors: \n"))

Rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
if user>2 or user<0:
    print("You entered an invalid option,please try again later ")
else:

      computer= random.randint(0,2)
      rock_paper_scissor=[Rock,Paper,Scissors]
      print(rock_paper_scissor[user])
      print(f"""Computer Chose: 
      {rock_paper_scissor[computer]}""")


 
      # 0-> Rock
      # 1-> Paper
      # 2-> Scissors



      if computer>user:
          if user==0 and computer == 2:
              print("You Win")
          else:
              print("You Lose")
      elif user>computer:
          if computer==0 and user==2:
              print("You Lose")
          else:
              print("You Win")
      else:
              print("It's a draw")



      