# Dataframe


<a href = "https://pandas.pydata.org/pandas-docs/stable/reference/frame.html">官方連結</a>


<ul>
    <li><a href = "https://nbviewer.jupyter.org/github/Eddie02582/Python/blob/master/pandas/Datafram/Create%20data%20and%20Basic%20operation.ipynb">Create data and Basic operation</a></li>
    <li><a href = "https://nbviewer.jupyter.org/github/Eddie02582/Python/blob/master/pandas/Datafram/Read%20data%20and%20Data%20selection.ipynb">Read data and Data selection</a></li>
    <li><a href = "https://nbviewer.jupyter.org/github/Eddie02582/Python/blob/master/pandas/Datafram/Data%20Filter.ipynb">Data Filter</a></li>
</ul>



## DataFrame Combine Data


### pd.concat
<a href = "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html">詳情可以參考 </a>
#### 資料欄位相同

```
>>> df1
   #        Player  GP   MIN   PTS   FGM   FGA   FG%  3PM   3PA   3P%   FTM   FTA   FT%  OREB  DREB  REB  AST  STL  BLK  TOV   EFF
0  1  James Harden  61  36.7  34.4   9.9  22.7  43.5  4.4  12.6  35.2  10.1  11.8  86.1   1.0   5.3  6.4  7.4  1.7  0.9  4.5  31.8
1  2  Bradley Beal  57  36.0  30.5  10.4  22.9  45.5  3.0   8.4  35.3   6.8   8.0  84.2   0.9   3.3  4.2  6.1  1.2  0.4  3.4  25.4
>>> df2
     #        Player  GP   MIN   PTS  FGM   FGA   FG%  3PM  3PA   3P%  FTM  FTA   FT%  OREB  DREB  REB  AST  STL  BLK  TOV   EFF
49  50  Terry Rozier  63  34.4  18.0  6.3  14.9  42.3  2.7  6.7  40.7  2.6  3.0  87.4   0.8   3.6  4.4  4.1  1.0  0.2  2.2  16.4
>>> pd.concat([df1,df2])
     #        Player  GP   MIN   PTS   FGM   FGA   FG%  3PM   3PA   3P%   FTM   FTA   FT%  OREB  DREB  REB  AST  STL  BLK  TOV   EFF
0    1  James Harden  61  36.7  34.4   9.9  22.7  43.5  4.4  12.6  35.2  10.1  11.8  86.1   1.0   5.3  6.4  7.4  1.7  0.9  4.5  31.8
1    2  Bradley Beal  57  36.0  30.5  10.4  22.9  45.5  3.0   8.4  35.3   6.8   8.0  84.2   0.9   3.3  4.2  6.1  1.2  0.4  3.4  25.4
49  50  Terry Rozier  63  34.4  18.0   6.3  14.9  42.3  2.7   6.7  40.7   2.6   3.0  87.4   0.8   3.6  4.4  4.1  1.0  0.2  2.2  16.4
>>>
```

使用ignore_index = True,注意index會自動往下排

```
>>> pd.concat([df1,df2],ignore_index = True)
    #        Player  GP   MIN   PTS   FGM   FGA   FG%  3PM   3PA   3P%   FTM   FTA   FT%  OREB  DREB  REB  AST  STL  BLK  TOV   EFF
0   1  James Harden  61  36.7  34.4   9.9  22.7  43.5  4.4  12.6  35.2  10.1  11.8  86.1   1.0   5.3  6.4  7.4  1.7  0.9  4.5  31.8
1   2  Bradley Beal  57  36.0  30.5  10.4  22.9  45.5  3.0   8.4  35.3   6.8   8.0  84.2   0.9   3.3  4.2  6.1  1.2  0.4  3.4  25.4
2  50  Terry Rozier  63  34.4  18.0   6.3  14.9  42.3  2.7   6.7  40.7   2.6   3.0  87.4   0.8   3.6  4.4  4.1  1.0  0.2  2.2  16.4
```

使用keys 區分不同份資料
```
>>> pd.concat([df1, df2], keys=['2019-2020', '2018-2019'])
             #        Player  GP   MIN   PTS   FGM   FGA   FG%  3PM   3PA  ...   FTA   FT%  OREB  DREB  REB  AST  STL  BLK  TOV   EFF
2019-2020 0  1  James Harden  61  36.7  34.4   9.9  22.7  43.5  4.4  12.6  ...  11.8  86.1   1.0   5.3  6.4  7.4  1.7  0.9  4.5  31.8
          1  2  Bradley Beal  57  36.0  30.5  10.4  22.9  45.5  3.0   8.4  ...   8.0  84.2   0.9   3.3  4.2  6.1  1.2  0.4  3.4  25.4
2018-2019 0  1  James Harden  61  36.7  36.0   9.9  22.7  43.5  4.4  12.6  ...  11.8  86.1   1.0   5.3  6.4  7.4  1.7  0.9  4.5  31.8
          1  2  Bradley Beal  57  36.0  25.0  10.4  22.9  45.5  3.0   8.4  ...   8.0  84.2   0.9   3.3  4.2  6.1  1.2  0.4  3.4  25.4
```
Label the index keys you create with the names option.


```
>>> pd.concat([df1, df2], keys=['2019-2020', '2018-2019'] , names = ["Season","ID"])
              #        Player  GP   MIN   PTS   FGM   FGA   FG%  3PM   3PA   3P%   FTM   FTA   FT%  OREB  DREB  REB  AST  STL  BLK  TOV   EFF
Season    ID
2019-2020 0   1  James Harden  61  36.7  34.4   9.9  22.7  43.5  4.4  12.6  35.2  10.1  11.8  86.1   1.0   5.3  6.4  7.4  1.7  0.9  4.5  31.8
          1   2  Bradley Beal  57  36.0  30.5  10.4  22.9  45.5  3.0   8.4  35.3   6.8   8.0  84.2   0.9   3.3  4.2  6.1  1.2  0.4  3.4  25.4
2018-2019 0   1  James Harden  61  36.7  36.0   9.9  22.7  43.5  4.4  12.6  35.2  10.1  11.8  86.1   1.0   5.3  6.4  7.4  1.7  0.9  4.5  31.8
          1   2  Bradley Beal  57  36.0  25.0  10.4  22.9  45.5  3.0   8.4  35.3   6.8   8.0  84.2   0.9   3.3  4.2  6.1  1.2  0.4  3.4  25.4
```



## DataFrame其他相關操作


### df.rename(rename_dic, axis=1)
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

### df.sort_values
<a href = "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html">詳細連結</a>

```
>>> df.sort_values(by=['Chinese','Chemistry'])
   Chemistry  Chinese  English  Math   Name  physics
2         50       40       50    80  Green       80
0         90       40       60    85  James       40
1         70       45       70    90  Davis       30
```


### df.set_index

```
>>> df.set_index(["#"])
                     Player  GP   MIN   PTS   FGM   FGA   FG%  3PM   3PA   3P%   FTM   FTA   FT%  OREB  DREB   REB   AST  STL  BLK  TOV   EFF
#
1              James Harden  61  36.7  34.4   9.9  22.7  43.5  4.4  12.6  35.2  10.1  11.8  86.1   1.0   5.3   6.4   7.4  1.7  0.9  4.5  31.8
2              Bradley Beal  57  36.0  30.5  10.4  22.9  45.5  3.0   8.4  35.3   6.8   8.0  84.2   0.9   3.3   4.2   6.1  1.2  0.4  3.4  25.4
3     Giannis Antetokounmpo  57  30.9  29.6  10.9  20.0  54.7  1.5   4.8  30.6   6.3  10.0  63.3   2.3  11.5  13.7   5.8  1.0  1.0  3.7  34.8
4                Trae Young  60  35.3  29.6   9.1  20.8  43.7  3.4   9.5  36.1   8.0   9.3  86.0   0.5   3.7   4.3   9.3  1.1  0.1  4.8  26.6
5            Damian Lillard  58  36.9  28.9   9.2  20.0  45.7  3.9   9.9  39.4   6.7   7.6  88.8   0.5   3.8   4.3   7.8  1.0  0.4  2.9  27.8
6               Luka Doncic  54  33.3  28.7   9.5  20.6  46.1  2.9   9.1  31.8   6.8   9.1  75.2   1.3   8.0   9.3   8.7  1.1  0.2  4.2  30.4
7         Russell Westbrook  53  35.9  27.5  10.7  22.6  47.4  1.0   3.8  25.4   5.1   6.5  77.7   1.8   6.3   8.0   7.0  1.7  0.3  4.5  26.7
8             Kawhi Leonard  51  32.2  26.9   9.3  19.9  46.9  2.1   5.7  36.6   6.1   6.9  88.9   1.0   6.3   7.3   5.0  1.8  0.6  2.7  27.5
9             Anthony Davis  55  34.3  26.7   9.2  18.1  51.1  1.2   3.5  33.5   7.0   8.3  84.5   2.3   7.1   9.4   3.1  1.5  2.4  2.5  30.5

```
### df.fillna("")   
```
df.fillna("")   
```
## Piviot

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
















