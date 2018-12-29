import sys

def hex_xor(hex_string1, hex_string2):
    xored_int = int(hex_string1, 16) ^ int(hex_string2, 16)
    return xored_int.to_bytes((xored_int.bit_length() + 7) // 8, 'big')

if __name__ == '__main__':
    print(hex_xor(sys.argv[1], sys.argv[2]).hex())
