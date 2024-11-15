from os import system, name

def clear():
    if name != 'nt':
        _ = system('clear')
    else:
        _ = system('cls')
