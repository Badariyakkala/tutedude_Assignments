from tkinter import *

window = Tk()
window.title("Pack Configurations")
window.geometry("300x300")

lbl = Label(window,text="label1",bg="red",fg="white")
lbl1 = Label(window,text="label1",bg="blue",fg="white")
lbl2 = Label(window,text="label1",bg="green",fg="white")
lbl.pack(side=TOP,fill=X,expand=1) #X means Horizanl and Y means Vertical,expand=0 will place label at corner =1 will be at middele.
lbl1.pack(side=BOTTOM,fill=X,expand=0)
lbl2.pack(side=LEFT,fill=Y,expand=0)

window.mainloop()