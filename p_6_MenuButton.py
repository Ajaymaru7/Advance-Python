from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x300")

def hindi():
    messagebox.showinfo("Hii","I m hindi...!!")

menubutton = Menubutton(root, text = "Language")

menubutton.grid()

menubutton.menu = Menu(menubutton)

menubutton["menu"] = menubutton.menu

menubutton.menu.add_checkbutton(label= "Hindi",command = hindi,variable=IntVar())

menubutton.pack()

root.menubutton()
