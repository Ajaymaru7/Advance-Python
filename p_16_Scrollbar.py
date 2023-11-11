from tkinter import*
root = Tk()
#root.geometry("300x300")

sb=Scrollbar(root)
sb.pack(fill=Y,side = LEFT)

sb1=Scrollbar(root,orient = HORIZONTAL)
sb1.pack(fill=X, side = BOTTOM)

L = Listbox(root,yscrollcommand = sb.set, xscrollcommand = sb.set)
L.pack()

for line in range(50):
    L.insert(END,"Your Lucky NUMBER Enter  : "+str(line))
sb.config(command = L.yview)
sb1.config(command = L.xview)
    
root.mainloop()
