from scripts.encode_png import encode_png
from scripts.file_type_decider import file_type_decider

def call_encoder(file_path,target_path):
    #get the file type of the specified file
    file_id=file_type_decider(file_path) #each file type has a uniue integer id
    if file_id==0:
        #TODO:print the file type in order to give more information
        print("Error: Unrecognized file type")
        return

    #call the appropriate decoder
    if file_id==1:
        encode_png(file_path)


