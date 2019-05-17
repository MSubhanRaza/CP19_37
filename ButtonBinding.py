
from tkinter import *
import random

mycolor = '#%02x%02x%02x' % (64, 204, 208)
mycolor2 = '#7825D0' 
window = Tk()
window.title("My Application")
window.configure(background=mycolor2)
window.minsize(300,100)
window.geometry("320x100")



def click_me():
    print("I have Clicked")

def click_color():
    #rd = random.randint(,200)
    rd = random.randrange(1,100000)
    clr = '#A'+str(rd)
    print(rd)
    window.configure(bg=clr)

btn = Button(window,text="Check",command=click_me)
btn.pack()

btn1 = Button(window,text="COLOR",command=click_color)
btn1.pack()

window.mainloop()


