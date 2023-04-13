from PIL import Image
from utils.string_to_binary import string_to_binary


def encode_png(file_path,message_path):
    image=Image.open(file_path,"r").convert("RGBA")
    message=open(message_path,"r").read()
    #TODO:finish the encoder for PNGs
