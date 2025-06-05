from tkinter import *

window = Tk()
window.title("Tkinter Window")
window.config(bg="Dark grey")
window.geometry("500x300")
inp = Label(window, text="Hello World using Tkinter")
inp.pack()


#Adding Frames to Window.
Frm = Frame(window,bg="blue",width=100,height=100,cursor="dotbox")
Frm1 = Frame(window,bg="red",width=100,height=100,cursor="dot")
Frm.pack(side=TOP)
Frm1.pack(side=LEFT)

btn = Button(Frm,text="Click Me",bg="green",fg="white",width=20,height=2)
btn1 = Button(Frm1,text="Click Me",bg="red",fg="white",width=20,height=2)
btn.pack(side=RIGHT)
btn1.pack(side=LEFT)
window.mainloop()