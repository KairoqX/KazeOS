from config import usrname
from calc import calc

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
            
        