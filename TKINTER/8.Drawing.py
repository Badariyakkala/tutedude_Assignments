import tkinter
from tkinter import *

window = Tk()

c= tkinter.Canvas()
c.pack()
c.create_line(0,0,500,500,fill="black",width=5)
c.create_rectangle(0,0,500,500,fill="red")
window.mainloop()
