from config import usrname
from calc import calc
from os_detection import clear_terminal
from ls_command import ls_command
import os

def usr_commands():
    while True:
        inpts = input(f"KairOS@{usrname}: ")

        if(inpts == "help"):
            print("""
            Available commands:
             help
             about
             calc
             clear
             exit
            """)
        elif (inpts == "exit"):
            print("closing qonsole....")
            break
        elif(inpts == "calc"):
            calc()
        elif(inpts == "clear"):
            clear_terminal()
        elif(inpts.startswith('ls')):
            ls_command(inpts)

        