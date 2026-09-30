from config import usrname
from calc import calc
from os_detection import clear_terminal
from commands import ls_command, cd_command, mkdir, rm, cat
import os

def usr_commands():
    while True:
        inpts = input(f"KazeOS@{usrname}: ")

        if(inpts == "help"):
            with open('help.txt', 'r') as f:
                content = f.read()
                print(content)
        elif (inpts == "exit"):
            print("closing qonsole....")
            break
        elif(inpts.startswith('calc')):
            calc(inpts)
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
        elif(inpts.startswith('mkdir')):
            mkdir(inpts)
        elif(inpts.startswith('rm')):
            rm(inpts)
        elif(inpts.startswith('cat')):
            cat(inpts)
            