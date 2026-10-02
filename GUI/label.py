from tkinter import *

window = Tk()

photo = PhotoImage(file='GUI/logo.png')
label = Label(
    window,
    text="kazeOS",
    font=('Arial',40,'bold'),
    fg='red',
    bg='black',
    relief=RAISED,
    bd=10,
    padx=20,
    pady=20,
    image=photo,
    compound="top"
)


label.pack()
window.mainloop()