#convert an ascii string into its binary representation
#take each charachter and convert it into 8 bits that represent it
#example abc->a b c->01100001 01100010 01100011->011000010110001001100011
def string_to_binary(input_string):
    return ''.join([bin(ord(i))[2:].zfill(8) for i in input_string])
