import os
def ls_command(x):
    dirname = x.split(" ")
    dir = dirname[1]

    print(os.listdir(dir))

