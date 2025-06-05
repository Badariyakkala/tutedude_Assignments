from tkinter import *

window = Tk()
window.title("Button Commands")
window.geometry("300x300")

def clickhere():
    print("Test")

btn = Button(window, text="Click Me", fg="red", bg="blue",command=clickhere,activebackground="green",activeforeground="black")
btn.pack()
window.mainloop()
