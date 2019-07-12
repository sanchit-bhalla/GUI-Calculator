from tkinter import *
import tkinter.messagebox as tmsg

def click(event):
    #   cget is used to get the text from (button) widget
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                scvalue.set(scvalue.get().replace("^","**"))   # bcz in python  operator for power is  **
                import math
                scvalue.set(scvalue.get().replace("e",f"{math.e}"))
                value = eval(scvalue.get())
            except:
                value = "Error!"
                scvalue.set(value)
                tmsg.showinfo("Error","Wrong input!")
        scvalue.set(value)
        screen.update()
        
    elif text == "C":
        scvalue.set("")
        screen.update()
    elif text == "X":
        scvalue.set(scvalue.get()[0:len(scvalue.get())-1])
    
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
    
    
root = Tk()
root.geometry("330x490")
root.wm_iconbitmap("calc.ico")
root.config(bg="grey")
root.title("My GUI CALCULATOR")

scvalue = StringVar()
scvalue.set("")
screen  = Entry(root,textvariable = scvalue, font="lucida 20 bold")
screen.pack(fill=X,ipadx=8,ipady=5,pady=10,padx=8)   # ipad is internal padding

f = Frame(root, bg="grey")
b=  Button(f,text="9",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)    # <Button-1>  is event for single click

b=  Button(f,text="8",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)

b=  Button(f,text="7",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)

b=  Button(f,text="6",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)    # <Button-1>  is event for single click

f.pack()



f = Frame(root, bg="grey")
b=  Button(f,text="5",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)

b=  Button(f,text="4",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)

b=  Button(f,text="3",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)    # <Button-1>  is event for single click

b=  Button(f,text="2",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)
f.pack()


f = Frame(root, bg="grey")
b=  Button(f,text="1",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)

b=  Button(f,text="0",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)    # <Button-1>  is event for single click

b=  Button(f,text="-",font="lucida 16 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=7)
b.bind("<Button-1>",click)

b=  Button(f,text="+",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=5)
b.bind("<Button-1>",click)
f.pack()



f = Frame(root, bg="grey")
b=  Button(f,text="*",font="lucida 17 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)    # <Button-1>  is event for single click

b=  Button(f,text="/",font="lucida 17 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)

b=  Button(f,text="%",font="lucida 14 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=4,ipady=4)
b.bind("<Button-1>",click)

b=  Button(f,text=".",font="lucida 17 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=7)
b.bind("<Button-1>",click)    # <Button-1>  is event for single click

f.pack()



f = Frame(root, bg="grey")
b=  Button(f,text="(",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=8)
b.bind("<Button-1>",click)

b=  Button(f,text=")",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=8)
b.bind("<Button-1>",click)

b=  Button(f,text = "^",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)    # <Button-1>  is event for single click

b=  Button(f,text="e",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)

f.pack()



f = Frame(root, bg="grey")
b=  Button(f,text="=",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)    # <Button-1>  is event for single click

b=  Button(f,text="C",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)

b=  Button(f,text="X",font="lucida 15 bold")
b.pack(side=LEFT, padx=10, pady =10,ipadx=6)
b.bind("<Button-1>",click)

b=  Button(f,text="exit",font="lucida 9 bold",command = root.destroy)
b.pack(side=LEFT, padx=10, pady =10,ipadx=4,ipady=7)
#b.bind("<Button-1>",click)
f.pack()

root.mainloop()
