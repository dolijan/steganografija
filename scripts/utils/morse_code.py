#we need to use the hardcoded dictionary

morse_dictionary = {".-": "A",
          "-...": "B",
          "-.-.": "C",
          "-..": "D",
          ".": "E",
          "..-.": "F",
          "--.": "G",
          "....": "H",
          "..": "I",
          ".---": "J",
          "-.-": "K",
          ".-..": "L",
          "--": "M",
          "-.": "N",
          "---": "O",
          ".--.": "P",
          "--.-": "Q",
          ".-.": "R",
          "...": "S",
          "-": "T",
          "..-": "U",
          "...-": "V",
          ".--": "W",
          "-..-": "X",
          "-.--": "Y",
          "--..": "Z"}

#it is possible to generate this dictionary programatically from morse_dictionary,
#however it will stay hardcoded for now
reverse_morse_dictionary={'A': '.-', 
            'B': '-...', 
            'C': '-.-.',
            'D': '-..', 
            'E': '.', 
            'F': '..-.', 
            'G': '--.', 
            'H': '....', 
            'I': '..', 
            'J': '.---', 
            'K': '-.-', 
            'L': '.-..', 
            'M': '--', 
            'N': '-.', 
            'O': '---', 
            'P': '.--.', 
            'Q': '--.-', 
            'R': '.-.', 
            'S': '...', 
            'T': '-', 
            'U': '..-', 
            'V': '...-', 
            'W': '.--', 
            'X': '-..-', 
            'Y': '-.--', 
            'Z': '--..'}


#takes a message and converts it inro a list where each list item 
#is a single charachter encoded in morse form
def encode_morse(plaintext):
    morse_code_message=[]
    plaintext=plaintext.upper()
    for c in plaintext:
        morse_code_message.append(reverse_morse_dictionary[c])
    return morse_code_message

#decodes a single charachter ".-"-> A
def decode_morse(charachter_string):
    return morse_dictionary[charachter_string]