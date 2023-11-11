from tkinter import*

top=Tk()
top.geometry("300x300")

P = PanedWindow(bg="Red",bd="3")
P.pack(fill = BOTH, expand = 1)

left = Label(P, text = "First",bg="Yellow")
P.add(left)

P1 = PanedWindow(P,orient=VERTICAL)
P.add(P1)

top = Label(P1, text = "second", bg='Green')
P1.add(top)



top.mainloop()
