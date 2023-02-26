import pywhatkit


def send_msg(contact_no:str,message:str):
    pywhatkit.sendwhatmsg_instantly(
        phone_no=contact_no, 
        message=message,
        tab_close= True, 
        close_time=10
        
        
    )
    
contact_no=['+917568561573','+917568561573','+917568561573','+917568561573','+917568561573','+917568561573','+917568561573','+917568561573','+917568561573','+917568561573','+917568561573','+917568561573','+917568561573']
msg=['Hi','Hello','Sure']
print(len(contact_no))
print(len(msg))
ctr=0
for i in range(0,len(contact_no)):
    for j in range(0,len(msg)):
        ctr+=1
        
        send_msg(contact_no[i],msg[j])
        print(f'Mesage sent to {contact_no[i]}')
print(ctr)
    
    