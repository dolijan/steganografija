from scripts.file_type_decider import file_type_decider
from scripts.png_encoder import encode_png
from scripts.unicode_encoder import encode_unicode

def call_encoder(file_path,message_path):
    #get the file type of the specified file
    file_id=file_type_decider(file_path) #each file type has a uniue integer id
    if file_id==0:
        #TODO:print the file type in order to give more information
        print("Error: Unrecognized file type")
        return

    #check that the message is a simple .txt file
    message_id=file_type_decider(message_path)
    if message_id!=2 and file_id!=1:
        #TODO:print the file type in order to give more information
        print("Message needs to be an ASCII text file (.txt)")
        return 

    #call the appropriate decoder
    if file_id==1:
        encode_png(file_path,message_path)
    elif file_id==3 or file_id==2:
        encode_unicode(file_path,message_path)
    


