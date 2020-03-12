# smtplib



## 寄信


``` python
import smtplib
from email.mime.text import MIMEText
from email.header import Header  

receivers_email = ["james@ttt.com"]
receivers_name = []
carbon_copy_email = []
carbon_copy_name = []
subject = "Test"
content = "Test Message"

mail_host= "172.31.7.240"  
mail_user= ""    
mail_pass= ""  

sender = 'eddie@ttt.com'  
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
```

如果要發送html格式將 MIMEText 'plain',修改成'html' 格式

```
content = "<p>Hi All</p>"
message = MIMEText(content, 'html', 'utf-8') 

```


## 夾檔

如要夾檔請用MIMEMultipart

``` python


message = MIMEMultipart()
message['Subject'] = Header(subject, 'utf-8')
message['From'] = Header("Eddie", 'utf-8')
message['To'] =  Header(','.join(receivers_name), 'utf-8')
message['CC'] =  Header(','.join(carbon_copy_name), 'utf-8') 


message.attach(MIMEText(msg, 'plain', 'utf-8'))

fp = open(filePath, 'rb')
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

夾圖檔

``` python

from email.MIMEImage import MIMEImage

message = MIMEMultipart()
message['Subject'] = Header(subject, 'utf-8')
message['From'] = Header("Eddie", 'utf-8')
message['To'] =  Header(','.join(receivers_name), 'utf-8')
message['CC'] =  Header(','.join(carbon_copy_name), 'utf-8') 

fp = open('test.jpg', 'rb')
message = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)   
    
```

如果圖片是要顯示在html,請在html新增
```
<img src="cid:image1"></img>
```

