from PIL import Image
from scripts.utils.string_to_binary import string_to_binary


#input_tuple is an RGBA value, this function takes a message and
#embedds 4 bits of it into the RGBA values of input_tuple
def embed(input_tuple,message,k):
    output_tuple=list(input_tuple)
    for i in range(4):
        if input_tuple[i]%2!=ord(message[k+i])-ord('0'):
            if ord(message[k+i])-ord('0')==0:
                output_tuple[i]=input_tuple[i]-1
            else:
                output_tuple[i]=input_tuple[i]+1

    return tuple(output_tuple)


def embed_message(pixels,message,n,m,mode,size):
    #build a new picture with appropriate LSBs
    encoded_picture=Image.new(mode,size)
    encoded_pixels=encoded_picture.load() #starting off with a blank picture
    
    #copy the content of the first image into the second one
    for i in range(n):
        for j in range(m):
            encoded_pixels[i,j]=(pixels[i,j][0],pixels[i,j][1],pixels[i,j][2],pixels[i,j][3])

    k=0
    #embed the message bit by bit
    #each charachter in message corresponds to 8 bits, so the message will
    #always be divisible by 4
    for i in range(n):
        for j in range(m):
            if len(message)<=k:
                return encoded_picture
            encoded_pixels[i,j]=embed(pixels[i,j],message,k)
            k+=4

    print(type(encoded_picture))
    return encoded_picture


def encode_png(file_path,message_path):
    image=Image.open(file_path,"r").convert("RGBA")
    pixels=image.load() #pixels is a matrix of 4-tuples
    n,m=image.size
    
    message_ascii=open(message_path,"rb").read().decode("latin-1")
    delimiter="$"+str(len(message_ascii))+"$" #we need a delimiter so that we can know how many charachter to read when decoding
    message=string_to_binary(delimiter+message_ascii)

    if len(message)>4*n*m:
        print("Error:The message is too big")
        return
    
    final_picture=embed_message(pixels,message,n,m,image.mode,image.size)


    final_picture.save(file_path.removesuffix('.png')+"_encoded.png")

