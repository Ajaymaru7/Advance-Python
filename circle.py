import tkinter
import random


c = tkinter.Canvas(width = 500, height = 500)
c.pack()

def click(event):
    r = 50
    x, y = event.x, event.y
    color = '#{:06x}'.format(random.randrange(256 ** 3))
    circ = c.create_oval(x - r, y - r, x + r, y + r, fill=color)

    def shrink(r, x, y, color, circ):
        if r > 0:
            r -= 1
            c.coords(circ, x-r, y-r, x+r, y+r)
            c.after(100, shrink, r, x, y, color, circ)

    shrink(r, x, y, color, circ)

c.bind('<Button-1>', click)
tkinter.mainloop()