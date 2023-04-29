#TODO:optimize this so that it does not read the whole message
#make it read the length first, and then only the required charachters
from PIL import Image

def decode_png(file_path):

    #until I implement more efficient decoding, this message will be printed
    print("Decoding, this may take a while......")

    image=Image.open(file_path,"r").convert("RGBA")
    pixels=image.load() #pixels is a matrix of 4-tuples
    n,m=image.size

    whole_message=""

    #we need to read the message 8 by 8 bits,hence the flag
    #(we need to update the message every two iterations)
    flag=True
    buffer="0b"
    for i in range(n):
        for j in range(m):
            buffer+=chr(pixels[i,j][0]%2+ord('0'))
            buffer+=chr(pixels[i,j][1]%2+ord('0'))
            buffer+=chr(pixels[i,j][2]%2+ord('0'))
            buffer+=chr(pixels[i,j][3]%2+ord('0'))
            if flag==True:
                flag=False
            else:
                flag=True
                whole_message+=chr(int(buffer,2))
                buffer="0b"

    if whole_message[0]!="$":
        print("Unknown error occured, please try again later")
        return
    
    #get the length of the encoded message from the delimiter
    length=0
    i=1
    while whole_message[i]!="$":
        length=10*length+(ord(whole_message[i])-ord('0'))
        i=i+1
    
    #get the indexes where our message lives
    i=i+1
    end_index=i+length

    #this is our file in binary, but latin-1 encoded
    message_latin_encoded=whole_message[i:end_index]


    #here we transform the message into bytes and save it into the file
    #TODO:add a file suffix, depending on the tipe of the encoded file
    #somehow manage to do that without saving the file first......
    print("Succesffully decoded the image.")
    
    file_path=file_path.removesuffix("_encoded.png")
    embedded_file_name=file_path.removesuffix(".png")+"_decoded"

    message_bytes=bytes(message_latin_encoded,"latin-1")
    file_new=open(embedded_file_name,"wb")
    file_new.write(message_bytes)
    
    file_new.close()