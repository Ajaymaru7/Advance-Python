from tkinter import*
def add():
    a=int(e1.get())
    b=int(e2.get())
    Left = str(a+b)
    left.insert(o.leftdata)

w1 = panedWindow()]
w1.pack(fill = BOTH,expand = 1)

left = Entry(w1, bd=5)
w1.add(left)

w2 = PanedWindow(w1, orient = VERTICAL)
w1.add(w2)

e1 = Entry(w2)
e2 = Entry(w2)

w2.add(e1)
w2.add(e2)

bottom = Buttom(w2, text="Add",command=add)
w2.add(bottom)

mainloop()
