from tkinter import *

root = Tk()

c = Canvas(root,bg='#091e42', width=2100, height=3600)

c.create_polygon(600,250,700,200,800,250,800,400,600,400, width=2, fill='yellow',outline='red')

c.create_line(600,250,800,250, width=2, fill='red')
c.create_rectangle(650,275,750,375, fill='red')

x1,y1 = 0,350
x2,y2 = 200,450

for i in range(3):
    c.create_arc(x1,y1,x2,y2, start=0, extent=180, fill='green')
    x1 += 200
    x2 += 200

c.create_arc(800,350,1000,450, start=0, extent=180, fill='green')
c.create_arc(1000,350,1200,450, start=0, extent=180, fill='green')


id = c.create_text(600,600,text = 'My Happy Home!', font=('Helvetica',30,'bold'),fill='magenta')

c.pack()
root.mainloop()