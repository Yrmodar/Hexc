import sys
import os

def binary():
    with open(filename,"rb")as file:
        offset = 0
        while True:
            chunk = file.read(16)
            if not chunk:
                break

            # ---- offset (8-digit hex) ----
            offset_str = "%08x" % offset

            # ---- hex column ----
            hex_left  = " ".join(["%02x" % b for b in chunk[:8]])
            hex_right = " ".join(["%02x" % b for b in chunk[8:]])
            hex_str   = (hex_left + "  " + hex_right).ljust(47)

            # ---- ASCII column ----
            ascii_str = ""
            for b in chunk:
                ascii_str += chr(b) if 32 <= b <= 126 else "."

            print(offset_str, " ", hex_str, " ", ascii_str)
            offset += 16

 #---- checks if command written properly ----
if len(sys.argv)==2:
    if sys.argv[1]=="-h":
        print("USAGE: python hexc.py <filename>")
    else:
        filename=sys.argv[1]     
        #---- checks if file exist ----
        if os.path.isfile(filename):
           binary()
        else:
            print("no such file enter valid file name ")
else:
    if len(sys.argv)>2:
        print("invalid Command \nuse python hexc.py -h for help")
    if len(sys.argv)==1:
        print("File name missing")
        