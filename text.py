import tkinter
from tkinter import *
#window = tkinter.Tk()
root = Tk()
root.geometry("500x500")
msg=Message(root,text="Welcome to Advance Python..!", bg="white",bd=5,relief = "groove",cursor = "dot",
               font = "arial 15 underline",fg = "black")
root.attributes('-alpha',0.6)

msg.place(x=130,y=140)
root.mainloop()
