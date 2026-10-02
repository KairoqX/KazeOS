from tkinter import *

count = 0
def click():
    global count
    count+=1
    label.config(text=count)
    # print(count)


window = Tk()
button = Button(window,text='click me')
button.config(command=click)
button.config(font=('Ink Free',50,'bold'))
button.config(bg='yellow')
button.config(fg="red")
button.config(activebackground='red')
button.config(activeforeground='yellow')
image = PhotoImage(file='GUI/logo.png')
button.config(image=image)
button.config(compound='top')
button.config(state=ACTIVE) #disables button ACTIVE or DISABLE
label = Label(window,text=count)
label.config(font=('Monospace',50))



label.pack()
button.pack()
window.mainloop()