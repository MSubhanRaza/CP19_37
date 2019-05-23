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