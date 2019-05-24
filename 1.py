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