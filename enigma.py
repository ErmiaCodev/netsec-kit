import random

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def rotate(stream: str) -> str:
    strm = stream[1:] + stream[0]
    return strm

def shufler(strm):
   s = list(strm)
   random.shuffle(s)
   return "".join(s)


def encode(rotors, plain):
    r1 = rotors[0]
    r2 = rotors[1]
    r3 = rotors[2]

    cipher = ""

    c = 0
    for char_ in plain:
        c += 1

        char_index = r1.find(char_)
        char_cipher = r2[char_index]

        char_index = r2.find(char_cipher)
        char_cipher = r3[char_index]

        cipher += char_cipher

        r1 = rotate(r1)

        if c % 4 == 0:
            r2 = rotate(r2)

        if c % 8 == 0:
            r3 = rotate(r3)

    return cipher

def decode(rotors, cipher):
    r1 = rotors[0]
    r2 = rotors[1]
    r3 = rotors[2]

    plain = ""

    c = 0

    for char_ in cipher:
        c += 1

        char_index = r3.find(char_)
        char_cipher = r2[char_index]

        char_index = r2.find(char_cipher)
        char_plain = r1[char_index]

        plain += char_plain

        r1 = rotate(r1)

        if c % 4 == 0:
            r2 = rotate(r2)

        if c % 8 == 0:
            r3 = rotate(r3)

    return plain
