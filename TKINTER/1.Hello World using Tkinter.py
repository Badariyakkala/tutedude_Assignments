#using Tkinter it helps to create GUI applications.

from tkinter import *
window = Tk()
window.title("Tkinter Window")
window.geometry("300x300") #--based on this we can dimension the window.
window.configure(bg="Sky blue",)
inp = Label(window,text="Hello World using Tkinter")
inp.pack() #this line is import to show text on window.
window.mainloop() ##_-This line is import to pop up window.
