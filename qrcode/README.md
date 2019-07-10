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
