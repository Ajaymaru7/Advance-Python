from tkinter import *
import random
app=Tk()

def canvas(event):
    my_list=["red","blue","white","purple","brown","pink","orange"]
    #my_list=["white"]
    x,y=event.x,event.y
    c.create_oval(x,x,y,y,fill=random.choice(my_list))

c=Canvas(app,width=1000,height=1000)
c.pack()
c.bind('<B3- Motion>',canvas)
app.mainloop()