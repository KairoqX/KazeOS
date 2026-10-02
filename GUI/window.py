from tkinter import *

window = Tk()
window.geometry("1280x720")
window.title("KazeOS")
icon = PhotoImage(file='GUI/logo.png')
window.config(background='black')

window.iconphoto(True,icon)
def new_win():
    nwin = Tk()
    # window.destroy()

Button(window, text='➕', command=new_win).pack()




window.mainloop()