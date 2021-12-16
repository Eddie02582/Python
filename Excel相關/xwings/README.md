# xwings 

## install 

```
    pip install xwings    
```

## Simple

``` python
import xlwings as xw
path = "simple.xlsx"
wb = xw.Book() 
sheet = wb.sheets[0] 
sheet.cells(1, 1).value = "first"
sheet.cells(1, 1).value = "second"
wb.save(path)
wb.close()
```


## workbook use

### open excel

if you want to create empty excel
``` python
wb = xw.Book() 
```

open exist excel
``` python
path = "simple.xlsx"
wb = xw.Book(path) 
```


save excel
```python
wb.save(path)
```


## how to get worksheet
可以透過index 取出
```
>>> wb.sheets[0]
<Sheet [simple.xlsx]Sheet1>
```

也可以透過sheetname

```
>>> wb.sheets["Sheet1"]
<Sheet [simple.xlsx]Sheet1>
```


## write value
```
sheet = wb.sheets[0]

```



### using index 

注意index 由1開始
```
sheet.cells(i, j).value = "test"; 
```

### using name 

```
sheet.range('B1').value = "test2"
```

### write range value

```
#write value from A2 ->E2
sheet.range('A2').value = [1,2,3,4,5]
```
也可以寫多行,但是筆數不一樣

```python
#write value from A2 ->E2
#write second array value from A3 ->C3
sheet.range('A2').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
```

如果想寫單欄

```python
sheet.range('A2').value = [[1], [2],[3]]
```

### write data using pandas/numpy

可以透過 expand() 方法，或是 options 方法的 expand 參數動態偵測並且讀取一個連續、有值的儲存格範圍的資料。<br>
這邊需要注意的是，expand() 方法會回傳一個 range() 物件，而 options(expand='table') 則會在選定一個範圍之後才會被執行<br>

```python
import pandas as pd
df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])

#下面方法在write 時並不影響
sheet.range('A1').options(expand='table').value = df
#sheet.range('A1').options().value
sheet.range('A1').expand('table').value = df #or just expand()

```

also can use numpy

```python
import numpy as np
arr = np.zeros(shape= (6,6))
for i in range(1,6):
    for j in range(1,6):
        arr[i - 1][j - 1] = i * j

sheet.range('A1').options(expend='table').value = arr
```






