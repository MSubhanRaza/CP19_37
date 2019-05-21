
from tkinter import *

def my_func():
    get_text = txt1.get()
    txt_welcome.delete(0,END)
    txt_welcome.insert(0,"WELOCOME : "+get_text)


form = Tk()
form.title("First App of Tkinter")
form.configure(background="gray")

lbl1 = Label(form,text="Please type your name here : ",fg="white",bg="gray",font="none 12 bold")
lbl1.grid(row=0,column=0,sticky=W)

txt1 = Entry(form,bg="white",width=35)
txt1.grid(column = 0,row = 1,sticky = W)

btn1 = Button(form,text="SUBMIT",command =my_func)
btn1.grid(column=0,row=2)



txt_welcome = Entry(form,width=35)
txt_welcome.grid(column = 0,row = 4, sticky = W)

form.mainloop()

