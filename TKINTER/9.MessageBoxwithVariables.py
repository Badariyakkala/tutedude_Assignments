import tkinter
from tkinter import *

window = Tk()

window.title("MessageBox With Variables")
window.geometry("500x500")

var = StringVar()
ent_var = StringVar()

def ShowText():
    res=ent_var.get()
    var.set(res)

message = Message(window, textvariable=var,padx=10,pady=10,relief=RAISED)
ent = Entry(window, textvariable=ent_var)
btn=Button(window, text="Show Text on Label", command=ShowText)
message.pack()
ent.pack()
btn.pack()
window.mainloop()


