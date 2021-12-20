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


## How to get worksheet
可以透過index 取出
```python
>>> wb.sheets[0]
<Sheet [simple.xlsx]Sheet1>
```

也可以透過sheetname

```python
>>> wb.sheets["Sheet1"]
<Sheet [simple.xlsx]Sheet1>
```


## How to write value
```python
sheet = wb.sheets[0]

```



### using index 

注意index 由1開始
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
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
sheet.range('A1').options(expand='table').value = df

```

### using index 

注意index 由1開始
```python
>>> sheet.cells(1, 2).value;
'a'
```

### using name 

```python
>>> sheet.range('B1').value
'a'
```

### read range value

```python
>>> sheet.range('A1:A3').value
[None, 0.0, 1.0]
>>> sheet.range('B2:D2').value
[0.014504139511606784, 0.846718191955516, 0.8054883506837824]
>>> sheet.range('B2:D11').value
[[0.014504139511606784, 0.846718191955516, 0.8054883506837824], [0.7203144951364651, 0.6543878396013
29659676, 0.3636829350305253, 0.9646241795964203], [0.8253046776251898, 0.4834959496769262, 0.595404
284357241831395, 0.35191345601387825], [0.5323093562134891, 0.24313480124914, 0.03008785394579394],
97, 0.8496090095955293]]
>>>
```

### read data to pandas data/numpy data
透過 expand() 方法，或是 options 方法的 expand 參數動態偵測並且讀取一個連續、有值的儲存格範圍的資料。<br>
這邊需要注意的是，expand() 方法會回傳一個 range() 物件，而 options(expand='table') 則會在選定一個範圍之後才會被執行<br>

```python
>>> sheet.range('A1').options(pd.DataFrame, header=1,index=True, expand='table').value
            a         b         c         d
0.0  0.014504  0.846718  0.805488  0.375279
1.0  0.720314  0.654388  0.818754  0.250473
2.0  0.133467  0.854283  0.133515  0.700129
3.0  0.815469  0.363683  0.964624  0.602132
4.0  0.825305  0.483496  0.595405  0.391589
5.0  0.953235  0.074340  0.878255  0.267074
6.0  0.442150  0.828436  0.351913  0.962466
7.0  0.532309  0.243135  0.030088  0.386585
8.0  0.653664  0.193904  0.745546  0.982367
9.0  0.129992  0.590118  0.849609  0.303577
>>>
```

read as numpy data
```python
>>> sheet.range('B1').options(np.array, expand='table').value
array([['a', 'b', 'c', 'd'],
       ['0.014504139511606784', '0.846718191955516',
        '0.8054883506837824', '0.3752791890872377'],
       ['0.7203144951364651', '0.6543878396013695', '0.818753747767004',
        '0.2504733123726084'],
       ['0.13346656513651933', '0.8542833214490047',
        '0.13351501992821024', '0.7001287380746833'],
       ['0.8154689029659676', '0.3636829350305253', '0.9646241795964203',
        '0.6021317626277647'],
       ['0.8253046776251898', '0.4834959496769262', '0.5954049789341439',
        '0.39158874716022307'],
       ['0.9532354667218765', '0.07434024495552216',
        '0.8782546497828244', '0.2670741487941871'],
       ['0.4421504006438578', '0.8284357241831395',
        '0.35191345601387825', '0.9624661015495203'],
       ['0.5323093562134891', '0.24313480124914', '0.03008785394579394',
        '0.38658483663817544'],
       ['0.6536636196907746', '0.1939040040617268', '0.7455460653157003',
        '0.9823669909015158'],
       ['0.12999199662429683', '0.5901178385921397',
        '0.8496090095955293', '0.30357656239359787']], dtype='<U20')
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













