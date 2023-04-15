from scripts.utils.morse_code import decode_morse

# '-' corresponds to zero width joiner
# '.' corresponds to zero width non joiner 

def decode_single_charachter(input_string):
    zero_width_joiner='\u200d'
    zero_width_non_joiner='\u200c'
    string_in_morse_format=""
    for c in input_string:
        if c==zero_width_joiner:
            string_in_morse_format+='-'
        else:
            string_in_morse_format+='.'
    return decode_morse(string_in_morse_format)

def decode_unicode(file_path):
    zero_width_joiner='\u200d'
    zero_width_non_joiner='\u200c'

    whole_text=open(file_path,"r").read()
    i=0
    buffer=""
    message=""
    while i<len(whole_text):
        if whole_text[i]==zero_width_joiner:
            buffer+=zero_width_joiner
            i=i+1
        elif whole_text[i]==zero_width_non_joiner:
            buffer+=zero_width_non_joiner
            i=i+1
        else:
            if buffer!="":
                message+=decode_single_charachter(buffer)
            buffer=""
            i=i+1

    print("Decoding completed. The secret message is:")
    print(message)