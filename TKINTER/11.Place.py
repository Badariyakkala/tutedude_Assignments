#Place is also similar to Grid and PACK
#in Pack we can place components in either TOP,BOTTOM,LEFT ,RIGHT
#In Grid we can place components in rows and columns

#but using place we can place components in desired X and Y dimensions.

from tkinter import *

window = Tk()
window.geometry("500x500")
btn = Button(window, text="Click Me")
btn.place(x=200, y=200)
window.mainloop()