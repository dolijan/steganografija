import sys
from scripts.file_type_decider import file_type_decider


#TODO: read a detailed help message from a file
def print_help_message():
    print("This is a help message")

def print_error_message(args):
    command=' '.join(args[1:])
    print("Unrecognized command "+command)
    print("Try \"steganografija --help\" for help")



if len(sys.argv)==1:
    print_help_message()

elif len(sys.argv)==2:
    if(sys.argv[1]=="-h" or sys.argv[1]=="--help"):
        print_help_message()
    else:
        print_error_message(sys.argv)

elif len(sys.argv)==3:
    if sys.argv[1]!='-d':
        print_error_message(sys.argv)
    else:
        file_id=file_type_decider(sys.argv[2]) #each file type has a unique integer id
        print(file_id) #print file id for now

elif len(sys.argv)==4:
    print_error_message(sys.argv)
    
elif len(sys.argv)==5:
    if sys.argv[1]!='-e':
        print_error_message(sys.argv)
    else:
        file_id=file_type_decider(sys.argv[2]) #each file type has a uniue integer id
        print(file_id) #print file id for now

else:
    print_error_message(sys.argv)


