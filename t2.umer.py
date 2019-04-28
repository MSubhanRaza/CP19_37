

from tkinter import *

master = Tk()


b = Button(master, text="log in", command=callback)
b.pack()
c = Button(master, text="log out", command=callback)
c.pack()


mainloop()

