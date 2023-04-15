#inserting zero width joiners and zero width non joiners to encode a 
#message in morse code (in order to save up space)

from scripts.utils.morse_code import encode_morse

# '-' corresponds to zero width joiner
# '.' corresponds to zero width non joiner 

def encode_char_with_joiners(char_in_morse):
    zero_width_joiner='\u200d'
    zero_width_non_joiner='\u200c'
    encoded_char=""
    for c in char_in_morse:
        if c=='-':
            encoded_char+=zero_width_joiner
        else:
            encoded_char+=zero_width_non_joiner
    return encoded_char
            

def encode_unicode(file_path,message_path):

    plaintext=open(file_path,"r").read()
    message=open(message_path,"r").read() #we have ensured that message is in ASCII format

    if len(message)>len(plaintext)+1:
        print("Error:Message is too large")
        return
    if len(message)==0:
        print("Error: Message is empty")
        return

    try: 
        morse_code=encode_morse(message)
    except:
        print("Error:Mesage has to be a string of english charachters without spaces")
    
    final_message=encode_char_with_joiners(morse_code[0])
    for i in range(len(plaintext)):
        final_message+=plaintext[i]
        if(i+1<len(message)):
            final_message+=encode_char_with_joiners(morse_code[i+1])
    

    encoded_file_name=file_path.removesuffix('.txt')+"_encoded.txt"
    
    try:
        encoded_file=open(encoded_file_name,"x")
        encoded_file.write(final_message)
    except:
        print("File with the name "+encoded_file_name+" already exists, please delete it before proceeding")

