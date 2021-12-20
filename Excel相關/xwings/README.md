# xwings 

<a href ="https://docs.xlwings.org/en/stable/">官網教學</a>

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

### open excel with app
visible 為是否要顯示excel,screen_updating為是否要更新螢幕,當screen_updating為False會比較省時間

```python
app = xw.App(visible =True, add_book=True)  
app.screen_updating = debug
app.display_alerts = False   
path = "simple.xlsx"
wb = xw.Book(path)  
    
```


## How to Manipulate worksheet

<a href = "https://docs.xlwings.org/en/stable/api.html#sheet">官網教學</a>

### get sheets/sheets
取得所有sheets
```python
>>> wb.sheets
Sheets([<Sheet [Book1]Sheet1>])
```

get shhet by index
```python
>>> wb.sheets[0]
<Sheet [simple.xlsx]Sheet1>
```

get shhet by sheetname
```python
>>> wb.sheets["Sheet1"]
<Sheet [simple.xlsx]Sheet1>
```

### add sheet
有三個參數
```python
add(name=None, before=None, after=None)
```
插入在sheet1之前

```python
wb.sheets.add('Sheet0',before = "Sheet1")
```
插入在Sheet1之後
```python
wb.sheets.add('Sheet2',after = "Sheet1")
```
### delete sheet
```python
>>> wb.sheets["Sheet2"].delete()
<Sheet [simple.xlsx]Sheet1>
```

### autofit sheet

<ul class="simple">
<li><p>To autofit rows, use one of the following: <code class="docutils literal notranslate"><span class="pre">rows</span></code> or <code class="docutils literal notranslate"><span class="pre">r</span></code></p></li>
<li><p>To autofit columns, use one of the following: <code class="docutils literal notranslate"><span class="pre">columns</span></code> or <code class="docutils literal notranslate"><span class="pre">c</span></code></p></li>
<li><p>To autofit rows and columns, provide no arguments</p></li>
</ul>


```python
import xlwings as xw
wb = xw.Book()
wb.sheets['Sheet1'].autofit('c')
wb.sheets['Sheet1'].autofit('r')
wb.sheets['Sheet1'].autofit()
```





## How to write value
```python
sheet = wb.sheets[0]
```

### using index 

使用座標(row,col),注意啟始位置從1開始
```python
sheet.cells(i, j).value = "test"; 
```

### using name 

```python
sheet.range('B1').value = "test2"
```

### write range value

```python
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

指定不要index,和head

```python
sheet.range('A1').options(expand='table',index=False, header=False).value = df

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


### write figure by Matplotlib 
```python
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot([1, 2, 3, 4, 5])
sheet.pictures.add(fig, name='MyPlot', update=True)
```

指定放置位置

```python
sheet.pictures.add(fig, name='MyPlot', update=True,left=sheet.range('B5').left, top=sheet.range('B5').top)

```

also can use pandas with matplotlib

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
ax = df.plot(kind='bar')
fig = ax.get_figure()
sheet.pictures.add(fig, name='MyPlot', update=True)
```


## How to read value

首先我們先寫個値進去
```python
import xlwings as xw
import pandas as pd
import numpy as np

path = "simple.xlsx"
wb = xw.Book() 
sheet = wb.sheets[0] 
sheet = wb.sheets[0]
df = pd.DataFrame(np.random.rand(5, 4), columns=['a', 'b', 'c', 'd'])
sheet.range('A1').options(expand='table').value = df

```

```python
>>> df
          a         b         c         d
0  0.921002  0.258183  0.417066  0.712426
1  0.854319  0.950455  0.655083  0.405378
2  0.731881  0.271852  0.002059  0.663275
3  0.215696  0.085970  0.155741  0.378884
4  0.783033  0.282854  0.561799  0.549592

```
### using index 

使用座標(row,col),注意index 由1開始
```python
>>> sheet.cells(2, 2).value
0.9210020590149163
```

### using name 
```python
>>> sheet.range('B2').value
0.9210020590149163
```

### read range value

### read col

```python
>>> sheet.range('B2:B6').value
[0.9210020590149163, 0.8543194171695255, 0.7318809859654273, 0.21569586136981367, 0.7830330228949836]
```

如果希望回傳2d list

```python
>>> sheet.range('B2:B6').options(ndim = 2).value
[[0.9210020590149163], [0.8543194171695255], [0.7318809859654273], [0.21569586136981367], [0.7830330228949836]]
```

### read row

```python
>>> sheet.range('B2:E2').value
[0.9210020590149163, 0.2581829142794191, 0.4170663337627397, 0.7124263358483016]
>>> sheet.range('B2:E6').value
```

如果希望回傳2d list
```python
>>> sheet.range('A2:E2').options(ndim=2).value
[[0.0, 0.9210020590149163, 0.2581829142794191, 0.4170663337627397, 0.7124263358483016]]
```

### read all
```python
sheet.range('B2:E6').value
```
也可以使用座標(row,col)

```python
sheet.range((2,2),(6,5)).value
```

using expand read,注意expand 是動態偵測並且讀取一個連續、有值的儲存格範圍,如果單讀在F7填値的話會抓取不到

```python
sheet.range('B2').expand().value
```

### read data by option/convert

#### numbers
```python
>>> sheet.range('A1').value
4.0
>>> sheet.range('A1').options(numbers=int).value
4
>>>
```
#### empty
```python
>>> sheet.range('B1').value
>>> sheet.range('B1').options(empty='NA').value
'NA'
```

#### read as dict

A :1
B :2

```python
>>> sheet.range('C1:D2').options(dict).value
{'A': 1.0, 'B': 2.0}
```

C D 
1 2 
```python
>>> sheet.range('C5:D6').options(dict, transpose=True).value
{'C': 1.0, 'D': 2.0}
```

### read data to pandas data/numpy data
透過 expand() 方法，或是 options 方法的 expand 參數動態偵測並且讀取一個連續、有值的儲存格範圍的資料。<br>
這邊需要注意的是，expand() 方法會回傳一個 range() 物件，而 options(expand='table') 則會在選定一個範圍之後才會被執行<br>

```python
>>> sheet.range('A1').options(pd.DataFrame, header=1,index=True, expand='table').value
            a         b         c         d
0.0  0.921002  0.258183  0.417066  0.712426
1.0  0.854319  0.950455  0.655083  0.405378
2.0  0.731881  0.271852  0.002059  0.663275
3.0  0.215696  0.085970  0.155741  0.378884
4.0  0.783033  0.282854  0.561799  0.549592
>>>
```

read as numpy data
```python
>>> sheet.range('B1').options(np.array, expand='table').value
array([['a', 'b', 'c', 'd'],
       ['0.9210020590149163', '0.2581829142794191', '0.4170663337627397',
        '0.7124263358483016'],
       ['0.8543194171695255', '0.9504553265761788', '0.6550831494071169',
        '0.4053778602050133'],
       ['0.7318809859654273', '0.27185191903152106',
        '0.0020588589304098015', '0.6632746573361699'],
       ['0.21569586136981367', '0.08597000792113141',
        '0.15574106685749678', '0.37888448435765365'],
       ['0.7830330228949836', '0.2828543736018313', '0.5617992477223079',
        '0.5495923143642101']], dtype='<U21')
>>>
```

### different options vs expand

```python
>>> sheet.range('A1').value = [[1,2], [3,4]]
>>> rng1 = sheet.range('A1').expand('table')
>>> rng2 = sheet.range('A1').options(expand='table')
>>> rng1
<Range [simple.xlsx]Sheet1!$A$1:$B$2>
>>> rng2
<Range [simple.xlsx]Sheet1!$A$1>
>>> rng1.value
[[1.0, 2.0], [3.0, 4.0]]
>>> rng2.value
[[1.0, 2.0], [3.0, 4.0]]
>>> sheet.range('A3').value = [5, 6]
>>> rng1.value
[[1.0, 2.0], [3.0, 4.0]]
>>> rng2.value
[[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]
>>>

```

## Wrire/Read Big Data

需要寫大量資料建議用datafram 或是np array,下列寫入100*100陣列,逐筆寫入需要121秒,一次寫入只需要1秒



```python
import xlwings as xw
import time
import pythoncom
import numpy as np
import pandas as pd

def write_value_by_cells():
    t1 = time.time() 
    debug = True
    app = xw.App(visible =debug, add_book=True)  
    app.screen_updating = debug
    app.display_alerts = False
    
    path = "test.xlsx"
    wb = xw.Book(path)    
    ws = wb.sheets[0]     
    for i in range(1,101):
        for j in range(1,101):
            ws.cells(i, j).value = i * j; 

    t2= time.time()
    print (t2 - t1)
    wb.save()
    wb.close()
    app.quit()



def write_value_by_range():
    t1 = time.time()
    
    debug = False
    app = xw.App(visible =debug, add_book=True)  
    app.screen_updating = debug
    app.display_alerts = False   
    wb = xw.Book()
    path = "test2.xlsx"   
    ws = wb.sheets[0] 
    
    arr = np.zeros(shape= (100,100))    
    for i in range(1,101):
        for j in range(1,101):
            arr[i - 1][j - 1] = i * j
    
    ws.range('A1').options(expend='table').value = arr     
    wb.save(path)
    wb.close()
    app.quit()
    
    t2= time.time()  
    print (t2 - t1)
 ```

如果遇到超時或內存錯誤,可以執行分塊,理想的塊大小將取決於您的系統和數組的大小，因此您必須嘗試幾種不同的塊大小以找到一種運行良好的塊大小：


```python
import pandas as pd
import numpy as np
sheet = xw.Book().sheets[0]
data = np.arange(75_000 * 20).reshape(75_000, 20)
df = pd.DataFrame(data=data)
sheet['A1'].options(chunksize=10_000).value = df
```

And the same for reading:
```python
# As DataFrame
df = sheet['A1'].expand().options(pd.DataFrame, chunksize=10_000).value
# As list of list
df = sheet['A1'].expand().options(chunksize=10_000).value
```




