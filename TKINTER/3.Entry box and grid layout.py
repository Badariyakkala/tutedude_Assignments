from tkinter import *

window = Tk()
window.title("Hello World using Tkinter")
window.geometry("300x300")
inp=Label(window,text="Mail",bg="Grey")
inp1=Label(window,text="Password",bg="Grey")
Ent = Entry(window, width=10)
Ent1 = Entry(window, width=10)
inp.grid(column=0,row=0)
inp1.grid(column=0,row=1)
Ent.grid(column=1,row=0)
Ent1.grid(column=1,row=1)
window.mainloop()