#


## Partial Argument Application
假設定義一個函數
```python
def multiply(x, y):
    return x * y
```
現在想返回某個數的double

```python
multiply(3, 2)
```
這樣每次都要傳入y = 2數値,於是重新定義一個函數呼叫他

```python
def double(x):
    return multiply(x,2)
```
python 提供另2種方法
```
double = lambda x: multiply(x, 2)
```
或是

```
from functools import partial
add_five = partial(multiply,y = 2)
```