from tkinter import *

root = TK()

topframe = frame(root)
topframe.pack()
bottomframe = frame(root)
bottomframe.pack(side=BOTTOM)

button1 = Button(topframe, text="button one", fg="black")
button2 = Button(topframe, text="button two", fg="black")
button3 = Button(bottomframe, text="button three", fg="black")
button4 = Button(bottomframe, text="button four", fg="black")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=BOTTOM)
button4.pack(side=BOTTOM)

root.mainloop()