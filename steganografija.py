import sys

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
    print("ovde ga dekodiramo")
elif len(sys.argv)==4:
    print_error_message(sys.argv)
elif len(sys.argv)==5:
    print("ovde ga enkodiramo")
else:
    print_error_message(sys.argv)


