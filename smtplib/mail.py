import smtplib
from email.mime.text import MIMEText
from email.header import Header   


def sendMail(subject,content,receivers_email,receivers_name,carbon_copy_email,carbon_copy_name): 
    mail_host="172.31.7.240"  
    mail_user= ""    
    mail_pass= ""  

    sender = 'howard_lai@sercomm.com'  
    receivers_email = carbon_copy_email + receivers_email       
   
    message = MIMEText(content, 'plain', 'utf-8')    
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("Eddie", 'utf-8')
    message['To'] =  Header(','.join(receivers_name), 'utf-8')
    message['CC'] =  Header(','.join(carbon_copy_name), 'utf-8')
  


    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)   
        #smtpObj.login(mail_user,mail_pass)       
        smtpObj.sendmail(sender, receivers_email, message.as_string())        
    except smtplib.SMTPException:
        print ("Error:")    
        



receivers_email = ["Eddie_Chuang@sercomm.com"]
receivers_name = []
carbon_copy_email = []
carbon_copy_name = []
subject = "Test"
content = "Test Message"

sendMail(subject,content,receivers_email,receivers_name,carbon_copy_email,carbon_copy_name)