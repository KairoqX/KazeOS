from qonsol import usr_commands
from config import usrname, password 


un_input = input("username: ").lower()
pass_input = input("password: ").lower()

if(un_input == usrname) and (pass_input == password):
    print("logged in...")
    usr_commands()

else:
    print("wrong")
    


