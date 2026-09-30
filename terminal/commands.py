import os
def ls_command(x):
    dirname = x.split(" ")
    dir = dirname[1]
    try:
        print(os.listdir(dir))
    except Exception:
        print("Location doesn't exist...")

def cd_command(a):
    dirname = a.split(" ")

    if a == 'cd':
        print("Provide the location of the directory...")
    else:    
        try:
            dir = dirname[1]
            os.chdir(dir)
        except Exception:
            print("Location doesn't exist...")

def mkdir(a):
    dirname = a.split(" ")

    if a == 'mkdir':
        print("Please enter a name for the folder...")
    else:
        try:
            dir = dirname[1]
            os.makedirs(dir)
        except FileExistsError:
            print("Folder already exists...")

            