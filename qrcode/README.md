# qrcode

## install 

```
    pip install qrcode
    pip install image
```


## easy create 


``` python
import qrcode 
//調用 qrcode.make() 方法傳入url 或者是想要顯示的內容
img = qrcode.make('http://www.baidu.com')
with open('test.png', 'wb') as f:
    img.save(f)
    
```



## create by parameter


``` python
import qrcode

data = 'https://www.google.com.tw/'
img_file = r'test.png'


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
傳入數據
qr.add_data(data)

qr.make(fit=True)

#生成二維條碼
img = qr.make_image()

保存
img.save(img_file)

img.show()
    
```


## add picture 


``` python
import qrcode
from PIL import Image

def getQRcode(data, file_name,icon_image=None):
    #實體化
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=4,
    )

    #傳入數據
    qr.add_data(data)
   
    qr.make(fit=True)
   
    #生成二維條碼
    img = qr.make_image(fill_color="blue", back_color="white")

    if icon_image:
        img=add_image(img,icon_image)
        
    img.save(file_name)
    img.show()
    return img
    
def add_image(img,icon_image):
   
    icon = Image.open(icon_image)
    
    img_w, img_h = img.size
    
    factor = 6
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    
    img.paste(icon, (w, h), mask=None)    
    return img
    
getQRcode('https://www.sercomm.com/home.aspx','test.png','icon.png')
    
```