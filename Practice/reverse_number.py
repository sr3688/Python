number_or_word=input("Enter a number to be reversed: ")

   
#234
#Using While
# rev=0
# number=int(number)
# while number>0:
#     num=number%10
#     rev=(rev*10)+num
#     number//=10
# # print(rev) 

#using for loop String
# rev=""
# ending=len(number)-1
# for num in range(0,len(number)):
    
#     rev+=number[ending]
#     ending-=1
    
    
# print(rev)

#Using for loop 
number_or_word_list=[]

for char in number_or_word:
    number_or_word_list.append(char)
# print(number_or_word_list)

# end=-1
ending=len(number_or_word_list)-1
number_or_word_list_reverse=[]
for index in range(0,len(number_or_word_list)):
    number_or_word_list_reverse.append(number_or_word_list[ending])
    ending-=1
    # end-=-1
# print(number_or_word_list_reverse)

number_or_word_list_reverse_string=""

for index in number_or_word_list_reverse:
    number_or_word_list_reverse_string+=index
print(f"Your reversed input is {number_or_word_list_reverse_string}")
def rev():
    inp=input("Enter: ")
    return inp[::-1]
print(rev())








    

        


      
