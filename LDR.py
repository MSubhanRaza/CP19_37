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
    