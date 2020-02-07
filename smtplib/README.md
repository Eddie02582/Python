# smtplib

## 寄信


``` python
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "mail server ip"  
mail_user= ""    
mail_pass= ""  

sender = 'from@ttt.com'

receivers_email = ["Eddie_Chuang@ttt.com","Admin@ttt.com"]
receivers_name = ["Eddie"]
carbon_copy_name = ["Admin"]
msg = "測試"

message = MIMEText(msg, 'plain', 'utf-8')
message['Subject'] = Header(subject, 'utf-8')
message['From'] = Header("Sercomm SEPU Web", 'utf-8')
message['To'] =  Header(','.join(receivers_name), 'utf-8')
message['CC'] =  Header(','.join(carbon_copy_name), 'utf-8')




try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)   
    #smtpObj.login(mail_user,mail_pass)       
    smtpObj.sendmail(sender, receivers_email, message.as_string())        
except smtplib.SMTPException:
    print ("Error:")    
    
```

## 夾檔
如要夾檔請用MIMEMultipart
``` python

mail_host = "mail server ip"  
mail_user= ""    
mail_pass= ""  

sender = 'from@ttt.com'


receivers_email = ["Eddie_Chuang@ttt.com","Admin@ttt.com"]
receivers_name = ["Eddie"]
carbon_copy_name = ["Admin"]

message = MIMEMultipart()

message['Subject'] = Header(subject, 'utf-8')
message['From'] = Header("Sercomm SEPU Web", 'utf-8')
message['To'] =  Header(','.join(receivers_name), 'utf-8')
message['CC'] =  Header(','.join(carbon_copy_name), 'utf-8')
message.attach(MIMEText(msg, 'plain', 'utf-8'))



fp = open(file, 'rb')
filename = os.path.basename(file)
attach = MIMEText(fp.read(), 'base64', 'utf-8')
attach["Content-Type"] = 'application/octet-stream'
attach["Content-Disposition"] = 'attachment; filename="%s"' %filename
message.attach(attach)

try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)   
    #smtpObj.login(mail_user,mail_pass)       
    smtpObj.sendmail(sender, receivers_email, message.as_string())        
except smtplib.SMTPException:
    print ("Error:")    
    
    
```