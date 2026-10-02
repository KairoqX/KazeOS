from tkinter import *

def submit():
    username = entry.get()
    print(f"Hellow {username}")

def delete():
    entry.delete(0,END)

window = Tk()

submit = Button(window,text='submit', command=submit)
delete = Button(window,text='delete', command=delete)

entry = Entry()
entry.config(font=("Ink Free", 50))
entry.config(bg="black",fg='red')
# entry.insert(0,"Enter Text") #default text
# entry.config(width=10, show='*')


delete.pack( )
submit.pack(side=RIGHT)
entry.pack()
window.mainloop()