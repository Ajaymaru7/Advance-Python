from tkinter import *
from tkinter import ttk

def left_click(event):
    print("Single click")
    
def double_click(event):
    print("double click")
    
widget=Button(None,text="click",font="Arial 20", bg="blue")
widget.pack()
widget.bind('<Button-1>',left_click)
widget.bind('<Double-1>',double_click)
widget.mainloop()
