from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Tkinter Window")

menubar = Menu(window)

FileMenu = Menu(menubar, tearoff=False)
def clickme():
    print("You clicked me")
FileMenu.add_command(label="New",command=clickme )
FileMenu.add_command(label="Save", command=clickme )
FileMenu.add_command(label="Save As", command=clickme )
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=window.destroy)

menubar.add_cascade(label="File", menu=FileMenu)
window.config(menu=menubar)
window.mainloop()
