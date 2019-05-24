lbl_LED1 = tk.Label(sec_frame,text="LED1",fg="#66FCF1")
lbl_LED1['bg']=sec_frame['bg']
lbl_LED1.config(font=("Segoe UI",12))
lbl_LED1.grid(row=1,column=1)

btn_LED1_on = tk.Button(sec_frame,text="ON",width=10)
btn_LED1_on.grid(row=1,column=2,padx=10)

btn_LED1_off = tk.Button(sec_frame,text="OFF",width=10)
btn_LED1_off.grid(row=1,column=3)

lbl_sp = tk.Label(sec_frame,text="",fg="#66FCF1",width="5")
lbl_sp['bg']=sec_frame['bg']
lbl_sp.config(font=("Segoe UI",12))
lbl_sp.grid(row=1,column=4)

logo5 = tk.PhotoImage(file="sidepic.png")
w5 = tk.Label(sec_frame, image=logo5)
w5['bg']=sec_frame['bg']
w5.grid(row=1,column=5,padx=10,pady=20,rowspan=4)