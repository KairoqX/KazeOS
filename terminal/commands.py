import os
def ls_command(x):
    dirname = x.split(" ")
    dir = dirname[1]
    print(os.listdir(dir))

def cd_command(a):
    dirname = a.split(" ")
    dir = dirname[1]
    os.chdir(dir)
