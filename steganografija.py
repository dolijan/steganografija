import sys
from scripts.decoder_parser import call_decoder
from scripts.encoder_parser import call_encoder

#TODO: read a detailed help message from a file
def print_help_message():
    print("This is a help message")

def print_error_message(args):
    command=' '.join(args)
    print("Unrecognized command: "+command)
    print("Try \"steganografija --help\" for help")


def get_cmd_arguments():
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
            return
        call_decoder(sys.argv[2])

    elif len(sys.argv)==4:
        print_error_message(sys.argv)
        
    elif len(sys.argv)==5:
        if sys.argv[1]!='-e':
            print_error_message(sys.argv)
            return
        if sys.argv[3]!='-m':
            print_error_message(sys.argv)
            return
        call_encoder(sys.argv[2],sys.argv[4])

    else:
        print_error_message(sys.argv)

get_cmd_arguments()