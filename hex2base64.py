import base64
import sys

def hex2base64(hex_string):
    return base64.b64encode(bytes.fromhex(hex_string))

if __name__ == '__main__':
    print(hex2base64(sys.argv[1]).hex())
