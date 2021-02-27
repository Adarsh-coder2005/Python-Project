from tkinter import *

def buttonClick(self):
    print('You have clicked me')

root = Tk()

f = Frame(root, height=200, width=300)
f.propagate(0)

f.pack()

b = Button(f, text='My Button', width=15, height=2, bg='Yellow', fg='blue')
b.pack()

b.bind("<Button-1>", buttonClick)

root.mainloop()