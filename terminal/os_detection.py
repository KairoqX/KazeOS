import os

os_family = os.name

def clear_terminal():
    if(os_family == "nt"):
        os.system('cls')

    elif(os_family == "posix"):
        os.system('clear')