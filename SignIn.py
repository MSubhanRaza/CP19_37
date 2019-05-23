
from tkinter import *


#----------------------------------LOGIN WINDOW CODE------------------------

#------------------BACKEND CODE------------------

def login():
    if(txt_username.get()=="admin")and(txt_pass.get()=="admin"):
        print("done")
        import Main
    else:
        lbl_message.config(text="Invalid Access",fg="red")


def des():
    window.destroy()

#---------------------GUI CODE--------------------

window = Tk()
window.minsize(300,200)
window.maxsize(300,200)
window.geometry("+400+220")
window.title("Smart Room System")
window.config(bg="#1f2833")

#---------------------CONTROLS GUI--------------------

lbl_title = Label(window,text="Sign In",fg="#66FCF1")
lbl_title.config(font=("Segoe UI bold",30))
lbl_title['bg'] = window['bg']
lbl_title.grid(row=0,column=0,columnspan=2)

lbl_username = Label(window,text="User Name",fg="#C5C6C7")
lbl_username.config(font=("Segoe UI",11))
lbl_username['bg'] = window['bg']
lbl_username.grid(row=1,column=0,padx=20,pady=8)

txt_username = Entry(window)
txt_username.grid(row=1,column=1,columnspan=2)

lbl_pass = Label(window,text="Password",fg="#C5C6C7")
lbl_pass.config(font=("Segoe UI",11))
lbl_pass['bg'] = window['bg']
lbl_pass.grid(row=2,column=0,padx=20,pady=8)

txt_pass = Entry(window,show="*")
txt_pass.grid(row=2,column=1,columnspan=2)

btn_login = Button(window,text="LOGIN",command=login)
btn_login.config(font=("Segoe UI",10))
btn_login.grid(row=3,column=1)

btn_cancel = Button(window,text="CANCEL",command=des)
btn_cancel.config(font=("Segoe UI",10))
btn_cancel.grid(row=3,column=2)

lbl_message = Label(window,text="")
lbl_message['bg'] = window['bg']
lbl_message.grid(row=4,column=0)

window.mainloop()

#---------------------LOGIN WINDOW CODE ENDS--------------------------------------

#---------------------MAIN WINDOW CODE BEGINS-------------------------------------

