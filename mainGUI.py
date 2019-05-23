
import Tkinter as tk
import sys
from gpiozero import LED
from gpiozero import LightSensor
import time

#---------------BACKEND CODE----------------
led1 = LED(21)
led2 = LED(26)
led3 = LED(13)




    
def LED2_On():
    led2.on()
    
def LED2_Off():
    led2.off()

def LED1_On():
    led1.on()
    
def LED1_Off():
    led1.off()
    
def LED3_On():
    led3.on()
    
def LED3_Off():
    led3.off()
    
flg = True    
    
def sample():
    #flg=True
    lbl_c_state.config(text="AUTO")
    btn_LED1_on.config(state="disable")
    btn_LED1_off.config(state="disable")
    btn_LED2_on.config(state="disable")
    btn_LED2_off.config(state="disable")
    btn_LED3_on.config(state="disable")
    btn_LED3_off.config(state="disable")
    
    ldr= LightSensor(7)
    if(ldr.value<0.5444)and(flg):
        led1.on()
        led2.on()
        led3.on()
    else:
        led1.off()
        led2.off()
        led3.off()
        #break
        print(ldr.value)
        
    root.after(500, sample)
    

def start():
    global flg
    flg = True
    sample()

def stop():
    global flg
    flg = False
    
    


def txt_a_change():
    lbl_c_state.config(text="AUTO")
    btn_LED1_on.config(state="disable")
    btn_LED1_off.config(state="disable")
    btn_LED2_on.config(state="disable")
    btn_LED2_off.config(state="disable")
    btn_LED3_on.config(state="disable")
    btn_LED3_off.config(state="disable")
    
    ldr= LightSensor(7)
    i=50000
    while i>=0 :
        if(ldr.value<0.5444):
            led1.on()
            led2.on()
            led3.on()
        else:
            led1.off()
            led2.off()
            led3.off()
            #break
        print(ldr.value)
        i -=1
        
    LED1_Off()
    LED2_Off()
    LED3_Off()

    

def txt_m_change():
    lbl_c_state.config(text="MANUAL")
    btn_LED1_on.config(state="normal")
    btn_LED1_off.config(state="normal")
    btn_LED2_on.config(state="normal")
    btn_LED2_off.config(state="normal")
    btn_LED3_on.config(state="normal")
    btn_LED3_off.config(state="normal")
    
    stop()


#-------------------------------------


root = tk.Tk()
root.title("Smart Room System")
root.config()
root.minsize(800,500)
root.maxsize(800,500)   
root.columnconfigure(2, weight=2)
# lbl_back = tk.Label(root,text="SMART ROOM SYSTEM",bg="red")
# lbl_back.config(font=("Segoe UI bold",30))
# lbl_back.pack(fill=tk.X)

#app = tk.Frame(root)
#app.grid()

#---------------------TITLE FRAME ----------------------



title_frame = tk.Frame(root,bg="#0B0C10")   
title_frame.grid(row=0,column=0,columnspan=3,sticky="ew")

logo1 = tk.PhotoImage(file="pic3.png")
w1 = tk.Label(title_frame, image=logo1)
w1['bg']=title_frame['bg']
w1.grid(row=0,column=0,padx=50)


lbl_title= tk.Label(title_frame,text="Smart Room System",fg="#45A29E")
lbl_title['bg']=title_frame['bg']
lbl_title.config(font=("Agency FB",30))
lbl_title.grid(row=0,column=1,columnspan=2)

lbl_slogan = tk.Label(title_frame,fg="white",text="Smart Way To Enlighten The World")
lbl_slogan['bg']=title_frame['bg']
lbl_slogan.config(font=("Segoe UI",10))
lbl_slogan.grid(row=1,column=1,pady=5)

sec_frame = tk.Frame(root,bg="#1F2833")
sec_frame.grid(row=1,column=0,columnspan=4,sticky="ew")

#------------STATE

# lbl_state = tk.Label(sec_frame,text="Current State Is : ",fg="#66FCF1")
# lbl_state['bg']=sec_frame['bg']
# lbl_state.config(font=("Segoe UI",12))
# lbl_state.grid(row=0,column=0,pady=10)

# lbl_c_state = tk.Label(sec_frame,text="Manual",fg="#66FCF1")
# lbl_c_state['bg']=sec_frame['bg']
# lbl_c_state.config(font=("Segoe UI",12))
# lbl_c_state.grid(row=0,column=1,pady=10)

btn_manual = tk.Button(sec_frame,text="MANUAL",bg="#45A29E",width=20,command=txt_m_change)
btn_manual.grid(row=0,column=1)

btn_auto = tk.Button(sec_frame,text="AUTO",bg="#45A29E",width=20,command=txt_a_change)
btn_auto.grid(row=0,column=2,columnspan=2,padx=0)

lbl_c_state = tk.Label(sec_frame,text="MANUAL",fg="#66FCF1")
lbl_c_state['bg']=sec_frame['bg']
lbl_c_state.config(font=("Segoe UI",15))
lbl_c_state.grid(row=0,column=5,pady=10)

#-----------LED 1

logo2 = tk.PhotoImage(file="LED.png")
w2 = tk.Label(sec_frame, image=logo2)
w2['bg']=sec_frame['bg']
w2.grid(row=1,column=0,padx=10,pady=20)

lbl_LED1 = tk.Label(sec_frame,text="LED1",fg="#66FCF1")
lbl_LED1['bg']=sec_frame['bg']
lbl_LED1.config(font=("Segoe UI",12))
lbl_LED1.grid(row=1,column=1)

btn_LED1_on = tk.Button(sec_frame,text="ON",command=LED1_On,width=10)
btn_LED1_on.grid(row=1,column=2,padx=10)

btn_LED1_off = tk.Button(sec_frame,command=LED1_Off,text="OFF",width=10)
btn_LED1_off.grid(row=1,column=3)

lbl_sp = tk.Label(sec_frame,text="",fg="#66FCF1",width="5")
lbl_sp['bg']=sec_frame['bg']
lbl_sp.config(font=("Segoe UI",12))
lbl_sp.grid(row=1,column=4)

logo5 = tk.PhotoImage(file="sidepic.png")
w5 = tk.Label(sec_frame, image=logo5)
w5['bg']=sec_frame['bg']
w5.grid(row=1,column=5,padx=10,pady=20,rowspan=4)

#-----------LED 2

logo3 = tk.PhotoImage(file="LED.png")
w3 = tk.Label(sec_frame, image=logo3)
w3['bg']=sec_frame['bg']
w3.grid(row=2,column=0,padx=0,pady=20)

lbl_LED2 = tk.Label(sec_frame,text="LED2",width=20,fg="#66FCF1")
lbl_LED2['bg']=sec_frame['bg']
lbl_LED2.config(font=("Segoe UI",12))
lbl_LED2.grid(row=2,column=1,padx=0,pady=30)

btn_LED2_on = tk.Button(sec_frame,text="ON",width=10,command=LED2_On)
btn_LED2_on.grid(row=2,column=2)

btn_LED2_off = tk.Button(sec_frame,text="OFF",width=10,command=LED2_Off)
btn_LED2_off.grid(row=2,column=3)

#-----------LED 3

logo4 = tk.PhotoImage(file="LED.png")
w4 = tk.Label(sec_frame, image=logo4)
w4['bg']=sec_frame['bg']
w4.grid(row=3,column=0,padx=0,pady=20)

lbl_LED3 = tk.Label(sec_frame,text="LED3",fg="#66FCF1")
lbl_LED3['bg']=sec_frame['bg']
lbl_LED3.config(font=("Segoe UI",12))
lbl_LED3.grid(row=3,column=1,padx=0,pady=20)

btn_LED3_on = tk.Button(sec_frame,text="ON",width=10,command=LED3_On)
btn_LED3_on.grid(row=3,column=2)

btn_LED3_off = tk.Button(sec_frame,text="OFF",width=10,command=LED3_Off)
btn_LED3_off.grid(row=3,column=3)


#--------------------FOOTER FRAME--------------------

ftr_frame = tk.Frame(root,bg="#0B0C10")
ftr_frame.grid(row=2,column=0,columnspan=4,sticky="ew")

# lbl_co = tk.Label(ftr_frame,text="Dessigned By : M Subhan Raza and Team",fg="#C5C6C7")
# lbl_co['bg']=ftr_frame['bg']
# lbl_co.grid(row=0,column=0,pady=0)

lbl_sp2 = tk.Label(ftr_frame,text="",width=113,fg="#66FCF1")
lbl_sp2['bg']=ftr_frame['bg']
lbl_sp2.grid(row=0,column=1,padx=200,pady=0)

exitPic = tk.PhotoImage(file="exit1.png")
btn_exit = tk.Button(ftr_frame,command=exit,image=exitPic,bg="#45A29E",width=100)
btn_exit.grid(row=0,column=1,pady=10)

#start.grid()
#stop.grid()

#root.after(1000, sample)
root.mainloop()


#----------------------

def exit():
    root.destroy()

