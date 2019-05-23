
from tkinter import *

window = Tk()
window.minsize(400,200)
window.geometry("+350+250")

def hide():
    window.withdraw()

def des():
    window.destroy()

def login():
    if(txt_name.get()=="admin")and(txt_pass.get()=="admin"):
        #print("I am logged in ")
        new_win = Toplevel(window)
        new_win.minsize(700,300)
        lbl_welcome = Label(new_win,text="Welcome to Smart Room Application")
        lbl_welcome.config(font=("Segoe UI",35))
        lbl_welcome.pack()
        btn_close = Button(new_win,text="EXIT",command=des)
        btn_close.pack()
        hide()
    else:
        lbl_message.config(text="Invalid Access",fg="red")
        




lbl_title = Label(window,text="LOGIN")
lbl_title.config(font=("Segoe UI",30))
lbl_title.grid(row=0,column=1)

lbl_name = Label(window,text="User Name ")
lbl_name.grid(row=1,column=1,sticky = W)
txt_name = Entry(window)
txt_name.grid(row=1,column=2,sticky=W)

lbl_pass = Label(window,text="Password ")
lbl_pass.grid(row=2,column=1,sticky = W)
txt_pass = Entry(window)
txt_pass.config(show="*")
txt_pass.grid(row=2,column=2,sticky=W)

ck_box = Checkbutton(window,text="Remeber the passowrd")
ck_box.grid(row=3,column = 1)


btn_login = Button(window,text = "LOGIN",command=login)
btn_login.grid(row=4,column=1)

lbl_message = Label(window,text="")
lbl_message.grid(row=5,column=1)

window.mainloop()

