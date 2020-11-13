#121=121
#abpba=abpba

number_or_word= input("Enter a number or a word to check if it is palindrome or not: ")

# length=len(number_or_word)
# long=length-1
# reverse=""
# for i in range(0,length):
#             reverse+=number_or_word[long]
#             long-=1
# if number_or_word==reverse:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

number_or_word_list=list()

for i in range(0,len(number_or_word)):
    number_or_word_list.append(number_or_word[i])

    
reverse_list=[]
end=len(number_or_word_list)-1

for i in range(0,len(number_or_word_list)):
    reverse_list.append(number_or_word_list[end])
    end-=1

if number_or_word_list==reverse_list:
    print(" This is a palindrome")
else:
    print("This is not a palindrome")



