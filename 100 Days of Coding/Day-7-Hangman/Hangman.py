import word_list 
import random
import hangman_art

print(hangman_art.hangman_title)

# Creating the word list and randomizing it.
guessed_list=[]
count_missed=0
missed_letter=""

word=random.choice(word_list.wordlist)

print("                         Welcome to the hangman \n ".upper())

# Creating list of dashes
for index in range(0,len(word)):
    guessed_list.append("_")

print("The word contains as many letters as the dashes below:\n")

# Printing the dashes as the letters in the word
for index in range(0,len(word)):
    print("_",end=" ")
print("\n")
print(word)


while(True):
    # Creating an empty string
    guessed_string=""

    # taking the input from the user and converting to lower case
    input_letter=input("Guess the letter or word: ").lower()
    

    # if the input is not alphabet
    if not input_letter.isalpha():
        print("Please enter the alphabet")
        exit()
    
    
    # if input is a letter or a word
    if input_letter in word or input_letter==word: 
        for index in range(0,len(word)):

            # if the input is a letter
            if input_letter== word[index]:
                guessed_list[index]=input_letter
                print(guessed_list[index],end=" ")

            # if the input is a word
            elif input_letter==word:
                guessed_list[index]=input_letter[index]
                print(guessed_list[index],end=" ")
                
            # if the input letter does not match with the word or word character
            else:
             print(guessed_list[index],end=" ")
        print()
    
    # if the input is not equal to word or not in word
    elif input_letter not in word or input_letter!=word :

            # the number of worng guess will be tracked and the wrong word guessed will be displayed

            missed_letter+=input_letter
            print(f"missed: {missed_letter}",)
            count_missed+=1
            missed_letter+=","
            print()  
    
    # Printing the hangman ascii art of number of  wrong guess   
    print(hangman_art.hangman[count_missed])
            
    # conversion of input which is in list into a string for comparision with the original word

    for index in range(0,len(guessed_list)):
        guessed_string+=guessed_list[index]
    print("\n")

    # comparing if the input is equal to the word
        
    if guessed_string == word:
       print("Game Over: You Win")
       exit()
    elif count_missed==6:
        print("Game Over: You Lost")
        exit()  
                 
    







        
    
        
        
        

        
        

            
        

    

        
    

    
    



    
        


