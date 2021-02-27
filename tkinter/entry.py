from tkinter import *
class MyEntry:
    def __init__(self, root):
        self.f = Frame(root, height=350, width=500)
        self.f.propagate(0)
        self.f.pack()

        self.l1 = Label(text='Enter User name: ')
        self.l2 = Label(text='Enter Password: ')

        self.e1 = Entry(self.f, width=25, fg='blue', bg='yellow', font=('Arial',14))

        self.e2 = Entry(self.f, width=25, fg='blue', bg='yellow', show='*')
        self.e2.bind('<Return>', self.display)

        self.l1.place(x=50, y=100)
        self.e1.place(x=200, y=100)
        self.l2.place(x=50, y=150)
        self.e2.place(x=200, y=150)

    def display(self, event):
        str1 = self.e1.get()
        str2 = self.e2.get()

        lbl1 = Label(text='Your name is: '+str1).place(x=50, y=200)
        lbl1 = Label(text='Your password is: '+str2).place(x=50, y=220)


root = Tk()

mb = MyEntry(root)

root.mainloop()