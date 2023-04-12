from scripts.decode_png import decode_png
from scripts.file_type_decider import file_type_decider

def call_decoder(file_path):
    #get the file type of the specified file
    file_id=file_type_decider(file_path) #each file type has a unique integer id
    if file_id==0:
        #TODO:print the file type in order to get more information
        print("Error : Unsupported file format")
        return
    
    #call the appropriate decoder
    if file_id==1:
        decode_png(file_path)
