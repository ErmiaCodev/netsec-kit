#!/bin/env python3
import asyncio

from colorama import Fore, Back, Style
from core import scan, auto_deauth, man_deauth
import os


def menu():
    os.system("clear")
    print(Fore.GREEN + "\t")
    print(Style.BRIGHT + \
          "\t▗▄ ▗▖           ▗▄▖                ▗▖ ▄▖  █       ")
    print("\t▐█ ▐▌      ▐▌  ▗▛▀▜                ▐▌▐▛   ▀   ▐▌  ")
    print("\t▐▛▌▐▌ ▟█▙ ▐███ ▐▙    ▟█▙  ▟██▖     ▐▙█   ██  ▐███")
    print("\t▐▌█▐▌▐▙▄▟▌ ▐▌   ▜█▙ ▐▙▄▟▌▐▛  ▘     ▐██    █   ▐▌  ")
    print("\t▐▌▐▟▌▐▛▀▀▘ ▐▌     ▜▌▐▛▀▀▘▐▌        ▐▌▐▙   █   ▐▌  ")
    print("\t▐▌ █▌▝█▄▄▌ ▐▙▄ ▐▄▄▟▘▝█▄▄▌▝█▄▄▌     ▐▌ █▖▗▄█▄▖ ▐▙▄ ")
    print("\t▝▘ ▀▘ ▝▀▀   ▀▀  ▀▀▘  ▝▀▀  ▝▀▀      ▝▘ ▝▘▝▀▀▀▘  ▀▀ ")
    print()
    print(Fore.WHITE + "\t{1}--Scan")
    print("\t{2}--Deauth")
    print("\t{3}--Manual Deauth")

    print("\t{9}--Exit")
    print()

while True:
    try:
        menu()

        prompt = input(Fore.BLUE + Style.BRIGHT + "enigma ~# " + Fore.WHITE + Style.NORMAL)

        if not prompt.isdigit():
            continue
        else:
            prompt = int(prompt)

        if prompt == 9:
            print("\nGood Bye :)")
            break

        elif prompt == 1:
            asyncio.run(scan())

        elif prompt == 2:
            asyncio.run(auto_deauth())
        
            
        elif prompt == 3:
            asyncio.run(man_deauth())
            
        

    except KeyboardInterrupt:
        print("\n\nGood Bye :)")
        break
    except EOFError:
        print("\n\nGood Bye :)")
        break
