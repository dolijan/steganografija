#TODO:Add magic to requirements.txt
import magic

#TODO:figure out how to be less dependent on python-magic
#Assigns an unique integer Id to a file depending on its tipe
#0:undefined
#1:PNG image
def file_type_decider(file_path):
    if str(magic.from_file(file_path)[0:3])=="PNG":
        return 1
    else:
        return 0