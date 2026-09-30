from config import usrname
from calc import calc
from os_detection import clear_terminal
from commands import ls_command, cd_command
import os

def usr_commands():
    while True:
        inpts = input(f"KazeOS@{usrname}: ")

        if(inpts == "help"):
            ...
        elif (inpts == "exit"):
            print("closing qonsole....")
            break
        elif(inpts == "calc"):
            calc()
        elif(inpts == "clear"):
            clear_terminal()
        elif(inpts == 'ls'):
            print(os.listdir())
        elif(inpts.startswith('ls')):
            ls_command(inpts)
        elif(inpts == 'pwd'):
            print(os.getcwd())
        elif(inpts.startswith('cd')):
            cd_command(inpts)
        