alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode(message,shift):
    encrypted_message=""
    
    for index in range(len(message)):

        if message[index]==" ":
                encrypted_message+=" "

        for alpha_index in range(len(alphabets)):
            if message[index]==alphabets[alpha_index]:
                encrypted_message+=alphabets[((alpha_index+shift)%26)]
            
    return encrypted_message
      
                
                

                    

def decode(message,shift):
    
    decrypted_message=""
    for index in range(len(message)):

        if message[index]==" ":
            decrypted_message+=" "

        for alpha_index in range(len(alphabets)):
            if message[index]==alphabets[alpha_index]:
                decrypted_message+=alphabets[(alpha_index-shift)%26]

    return decrypted_message
                 
        
