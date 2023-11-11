from tkinter import*
def selection():
    selection = "You "+str(radio.get())
    lable.config(text = selection)
top = Tk()

radio = IntVar()

lbl = Label(text = " : "), lbl.pack(), r1 = Radiobutton(top,
text="C",variable=radio,value=1,command=selection) r1.pack(another = W)
r1 = Radiobutton(top, text="C",variable=radio,value=2,command=selection)
r2.pack(another = W) r2 = Radiobutton(top,
text="C",variable=radio,value=3,command=selection)

r2.pack(anchor=W)
lable = Lable(top)
lable.pack()
top.mainloop()


