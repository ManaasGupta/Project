import smtplib
from email.message import EmailMessage
def email_alert(subject:str,body:str,to:str):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to
    
    user_email='exampleemail4use@gmail.com' # put your email here
    msg['from']=user_email
    app_password='ioneoldqhgmwzibn' #put your APP Password 
    
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(user_email,app_password)
    server.send_message(msg)
    print(f'Email Sent to {to}')
    server.quit()
if __name__=='__main__':
    email_list=['manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com','manasgpt3@gmail.com',]
    print(len(email_list))
    ctr=0
    for i in range(0,len(email_list)):
        ctr+=1
        email_alert('New_Test','Lets Test','manasgpt3@gmail.com')
    
    print(f'Email sent to {ctr} people ')