from tkinter import *

root = Tk()

c = Canvas(root, bg='white', height=700, width=1200)

file1 = PhotoImage(file="cat.gif")
file2 = PhotoImage(file="puppy.gif")
id = c.create_image(20,20,anchor=NW, image=file2)

c.pack()
root.mainloop()