from tkinter import *

window = Tk()
window.geometry("300x400")
ent = Entry(window,width=20,borderwidth=5)

def click(num):
    res=ent.get()
    ent.delete(0,END)
    ent.insert(0, str(res)+ str(num))

btn1 = Button(window,text="1",width=3,height=1,command=lambda:click(1))
btn1.place(x=0,y=100)
btn2 = Button(window,text="2",width=3,height=1,command=lambda:click(2))
btn2.place(x=40,y=100)
btn3 = Button(window,text="3",width=3,height=1,command=lambda:click(3))
btn3.place(x=80,y=100)
btn4 = Button(window,text="4",width=3,height=1,command=lambda:click(4))
btn4.place(x=0,y=150)
btn5 = Button(window,text="5",width=3,height=1,command=lambda:click(5))
btn5.place(x=40,y=150)
btn6 = Button(window,text="6",width=3,height=1,command=lambda:click(6))
btn6.place(x=80,y=150)
btn7 = Button(window,text="7",width=3,height=1,command=lambda:click(7))
btn7.place(x=0,y=200)
btn8 = Button(window,text="8",width=3,height=1,command=lambda:click(8))
btn8.place(x=40,y=200)
btn9 = Button(window,text="9",width=3,height=1,command=lambda:click(9))
btn9.place(x=80,y=200)
btn0 = Button(window,text="0",width=3,height=1,command=lambda:click(0) )
btn0.place(x=0,y=250)

def calc(math):
    inp = ent.get()
    ent.delete(0, END)
    global i,operator
    operator = math
    i = int(inp)



btn10 = Button(window,text="+",width=3,height=1,command=lambda:calc('+') )
btn10.place(x=40,y=250)
btn11 = Button(window,text="-",width=3,height=1,command=lambda:calc('-') )
btn11.place(x=80,y=250)

def res():
    output= int(ent.get())
    ent.delete(0,END)
    if operator == "+":
        ent.insert(0,i + output)
    elif operator == "-":
        ent.insert(0,i - output)
    elif operator == "*":
        ent.insert(0,i * output)
    elif operator == "/":
        ent.insert(0,i / output)

btn14 = Button(window,text="*",width=3,height=1,command=lambda:calc('*'))
btn14.place(x=0,y=300)

btn15 = Button(window,text="/",width=3,height=1,command=lambda:calc('/'))
btn15.place(x=40,y=300)

btn12 = Button(window,text="=",width=3,height=1,command=res)
btn12.place(x=80,y=300)

def clear():
    ent.delete(0,END)

btn13 = Button(window,text="Clear",width=3,height=1,command=clear)
btn13.place(x=0,y=350)

ent.place(x=0,y=50)
window.mainloop()
