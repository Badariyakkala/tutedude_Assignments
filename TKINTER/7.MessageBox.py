from tkinter import *
import tkinter.messagebox

window = Tk()

tkinter.messagebox.showinfo("Info", "Low Disk Space")
tkinter.messagebox.showwarning("Info", "Low Disk Space")
tkinter.messagebox.showerror("Info", "Low Disk Space")

Ans = tkinter.messagebox.askyesno("Warning Message", "Format Disc")

if Ans:
    print("Disc Formatted")
else:
    print("Disc Not Formatted")
window.mainloop()
