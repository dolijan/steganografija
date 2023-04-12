from scripts.decode_png import decode_png

def call_decoder(file_path,file_id):
    if file_id==1:
        decode_png(file_path)
