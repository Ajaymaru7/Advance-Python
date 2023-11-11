from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("200x200")

def hindi():
    messagebox.showinfo("Hii","I m your fav subjct...!!")

menubutton = Menubutton(top, text = "bca-6")

menubutton.grid()

menubutton.menu = Menu (menubutton)

menubutton ["menu"] = menubutton.menu

menubutton.menu.add_checkbutton(label = "Anroid",command = hindi,variable=IntVar())
menubutton.menu.add_checkbutton(label = "DW",command = hindi,variable=IntVar())
menubutton.menu.add_checkbutton(label = "Python",command = hindi,variable=IntVar())


menubutton.pack()

top.mainloop()
