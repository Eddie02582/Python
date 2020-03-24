# Dataframe

## 建立DataFrame

### array
```
arr = [["Math",85], ["Chemistry",90], ["Chinese",40],["physics",40],["English",60]]
df = pd.DataFrame(map, columns = ["subject", "scores"])# 指定欄標籤名稱  

```

Output :
```
      subject  scores
0       Math      85
1  Chemistry      90
2    Chinese      40
3    physics      40
4    English      60
```


### dictionary
```
subjects = ["Math", "Chemistry", "Chinese","physics","English"]  
scores = [85, 90, 40, 40, 60]  
map  = {"subject": subject,  
        "scores": scores
       }

df = pd.DataFrame(map)
```

Output :
```
      subject  scores
0       Math      85
1  Chemistry      90
2    Chinese      40
3    physics      40
4    English      60
```
若使用col,則是選擇dict to df 的欄位
```
pd.DataFrame(map,columns = ["subject"])
```


Output:
```
     subject
0       Math
1  Chemistry
2    Chinese
3    physics
4    English
```
### dictionary array


```
map  = [{ 'Name':'James','Math': 85,'Chemistry': 90,'Chinese': 40,'physics':40,'English': 60},
        { 'Name':'Davis','Math': 90,'Chemistry': 70,'Chinese': 45,'physics': 30, 'English': 70},
        { 'Name':'Green','Math': 80,'Chemistry': 50,'Chinese': 40,'physics': 80, 'English': 50},
       ]
  
df = pd.DataFrame(map,columns = ['Name','Math','Chemistry','Chinese','physics','English'])
```

Output:
```
    Name  Math  Chemistry  Chinese  physics  English
0  James    85         90       40       40       60
1  Davis    90         70       45       30       70
2  Green    80         50       40       80       50
```

## DataFrame 操作

### 資料描述查看
<ul>
    <li>shape</li>
    <li>describe()</li>
    <li>head()</li>
    <li>tail()</li>
    <li>columns</li>
</ul>
head,tail使用python slice 就可以取代

```
-----------------------------------------------------
df.shape
(3, 6)
-----------------------------------------------------
df.describe()
       Math  Chemistry    Chinese    physics  English
count   3.0        3.0   3.000000   3.000000      3.0
mean   85.0       70.0  41.666667  50.000000     60.0
std     5.0       20.0   2.886751  26.457513     10.0
min    80.0       50.0  40.000000  30.000000     50.0
25%    82.5       60.0  40.000000  35.000000     55.0
50%    85.0       70.0  40.000000  40.000000     60.0
75%    87.5       80.0  42.500000  60.000000     65.0
max    90.0       90.0  45.000000  80.000000     70.0
-----------------------------------------------------
df.columns
Index(['Name', 'Math', 'Chemistry', 'Chinese', 'physics', 'English'], dtype='object')
-----------------------------------------------------
```
### DataFrame一般操作


#### df.rename(rename_dic, axis=1)
用來修改欄位名稱,詳情可以參考<a href = "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html">df.rename</a>

```
#指定修改col
>>> df.rename(columns = {'Name':'First Name','English':"Sport"})
  First Name  Math  Chemistry  Chinese  physics  Sport
0      James    85         90       40       40     60
1      Davis    90         70       45       30     70
2      Green    80         50       40       80     50

#透過設定axis=1 指定修改col,axis = 0 為index

>>> df.rename({'Name':'First Name','English':"Sport"},axis=1)
  First Name  Math  Chemistry  Chinese  physics  Sport
0      James    85         90       40       40     60
1      Davis    90         70       45       30     70
2      Green    80         50       40       80     50

#也可以使用
df.columns = ['First Name','Math','Chemistry','Chinese','physics','Sport'] 
```

#### df.sort_values
<a href = "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html">詳細連結</a>

```
>>> df.sort_values(by=['Chinese','Chemistry'])
   Chemistry  Chinese  English  Math   Name  physics
2         50       40       50    80  Green       80
0         90       40       60    85  James       40
1         70       45       70    90  Davis       30
```

### DataFrame 資料選取

#### df['col_name'] or df[['col_name1','col_name2']]

```
>>> df['Name']
0    James
1    Davis
2    Green
Name: Name, dtype: object

>>> df[['Name','Math']]
    Name  Math
0  James    85
1  Davis    90
2  Green    80
```

#### df.iloc

##### df.iloc[row][col]
```
>>> df.iloc[0]
Name         James
Math            85
Chemistry       90
Chinese         40
physics         40
English         60
Name: 0, dtype: object

>>> df.iloc[0][1]
85
```
##### df.iloc[row_array,col_array]

```
>>> df.iloc[[0,2]]
   Chemistry  Chinese  English  Math   Name  physics
0         90       40       60    85  James       40
2         50       40       50    80  Green       80
>>> df.iloc[[0,2],[0,1]]
   Chemistry  Chinese
0         90       40
2         50       40
>>> df.iloc[[0,2],[0,1]]
```

##### df.iloc 切片
```
>>> df.iloc[:2,0:2]
   Chemistry  Chinese
0         90       40
1         70       45
```
```
>>> df.iloc[1:3,:]
    Name  Math  Chemistry  Chinese  physics  English
1  Davis    90         70       45       30       70
2  Green    80         50       40       80       50
```

#### df.loc[row_index]/df.loc[row_index][col_name]
用法跟df.iloc 類似但是使用名稱
```
>>> df.loc[0]
Name         James
Math            85
Chemistry       90
Chinese         40
physics         40
English         60
Name: 0, dtype: object
>>> df.loc[0,"Math"]
85
>>> df.loc[:,"Name":"Math"]
    Name  Math
0  James    85
1  Davis    90
2  Green    80
>>> df.loc[1:3,:]
    Name  Math  Chemistry  Chinese  physics  English
1  Davis    90         70       45       30       70
2  Green    80         50       40       80       50
>>>
```

### DataFrame 資料過濾

#### df[col_name].isin(array)
判斷col_name 値是否在array內,回傳格式如下
```
>>> df["Name"].isin(["James","Davis"])
0     True
1     True
2    False
Name: Name, dtype: bool
```

使用方式如下
```
>>> filter = df["Name"].isin(["James","Davis"])
>>> df[filter]
   Chemistry  Chinese  English  Math   Name  physics
0         90       40       60    85  James       40
1         70       45       70    90  Davis       30
```

#### df[col_name].str.contains(str, na=False)  
```
>>> filter = df["Name"].str.contains("s", na=False)
>>> df[filter]
   Chemistry  Chinese  English  Math   Name  physics
0         90       40       60    85  James       40
1         70       45       70    90  Davis       30
```

#### df[col_name].lt (lt,le,gt,ge,eq)
```
>>> df[df["English"].le(60)]
   Chemistry  Chinese  English  Math   Name  physics
0         90       40       60    85  James       40
2         50       40       50    80  Green       80
```



### Piviot

```
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv()
     Channel  Pathloss  ATTENUATOR  ANGLE       DIR  Thruput
0       2412       -99           0    NaN  DownLink     27.4
1       2412       -99           0    NaN    UpLink     27.6
2       2412       -99           0    NaN     Tx/Rx     34.3
3       2412       -99           1    NaN  DownLink     39.9
..       ...       ...         ...    ...       ...      ...
330     2412       -99         110    NaN  DownLink      0.0
331     2412       -99         110    NaN    UpLink      0.0
332     2412       -99         110    NaN     Tx/Rx      0.0
colNames = list(df.columns)


data = pd.pivot_table(df,index='ATTENUATOR',values = ["Thruput"],columns = ['DIR','Channel'],aggfunc = np.max)

data = pd.pivot_table(df,index=['ATTENUATOR','Channel'],values = ["Thruput"],columns = ['DIR'],aggfunc = np.max)

            Thruput
DIR        DownLink  Tx/Rx UpLink
Channel        2412   2412   2412
ATTENUATOR
0              27.4   34.3   27.6
1              39.9   34.7   28.0
2              25.6   37.1   20.3
...             ...    ...    ...
109             0.0    0.0    0.0
110             0.0    0.0    0.0


ax = data.plot(kind="line",grid=True).set_title("ATTENUATOR vs ThroughtPut")
#fig = ax.get_figure()	
#fig.set_size_inches(12,9)
plt.show()
            
```


## 讀取外部資料

### 讀取DataFrame














