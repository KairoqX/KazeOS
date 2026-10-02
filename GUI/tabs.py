from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("1280x720")
window.title("KazeOS")
icon = PhotoImage(file='GUI/logo.png')
window.config(background='black')

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1,text='Tab 1')
notebook.add(tab2,text='Tab 2')
notebook.pack(expand=True,fill='both')

Label(tab1,text='hello1',width=50,height=50).pack()


window.mainloop()