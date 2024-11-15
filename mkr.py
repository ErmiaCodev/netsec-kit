#!/bin/env python3

import pickle
from enigma import shufler

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"

lenght = 62

stream = lower + upper + nums

rotor1 = shufler(stream)
rotor2 = shufler(stream)
rotor3 = shufler(stream)


with open ("./data/rotors.dat", "wb") as f:
    data = [rotor1, rotor2, rotor3]
    pickle.dump(data, f)
