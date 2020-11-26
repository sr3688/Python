import encode_decode
import caesar_cipher_art

print(caesar_cipher_art.logo)

carryon=True
while(carryon):

    encode_decode_text=input("Type ' 'encode' or 'e' ' to encode and ' 'decode' or 'd' ' to decode: ").lower()
    print()
   
    if encode_decode_text=="encode" or encode_decode_text=="e":

        message=input("Enter the message to be encoded: ")
        print()
        message_code=int(input("Enter the message code: "))
        print()
        type_casted_message=""
        
        if message.isupper():
            type_casted_message=message.lower()
            encrypted_message=encode_decode.encode(type_casted_message,message_code)

        else:
             encrypted_message=encode_decode.encode(message,message_code)
        
        if message.isupper():
            print(encrypted_message.upper())
            
        else:
            print(encrypted_message)

        

    elif encode_decode_text=="decode" or encode_decode_text=="d":

        message=input("Enter the message to be decoded: ")
        print()
        message_code=int(input("Enter the message code: "))
        print()
        
        type_casted_message=""

        if message.isupper():

            type_casted_message=message.lower()
            decrypted_message=encode_decode.decode(type_casted_message,message_code)

        else:
            decrypted_message=encode_decode.decode(message,message_code)

        if message.isupper():
            print(decrypted_message.upper())

        else:
            print(decrypted_message)
        
    do_continue=input("Do you want to continue encoding or decoding? Yes or No ")

    if do_continue.lower()=='n' or do_continue.lower()=='no':
       carryon=False

        
        
        
        
 




    





        


    



