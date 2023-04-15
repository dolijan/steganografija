import magic

#TODO:figure out how to be less dependent on python-magic
#Assigns an unique integer Id to a file depending on its tipe
#0:undefined
#1:PNG image
#2:ASCII text
#3:Unicode text
def file_type_decider(file_path):
    if str(magic.from_file(file_path)[0:3])=="PNG":
        return 1
    elif str(magic.from_file(file_path))=="ASCII text" or str(magic.from_file(file_path))=="ASCII text, with no line terminators":
        return 2
    elif str(magic.from_file(file_path))=="Unicode text, UTF-8 text":
        return 3
    else:
        return 0