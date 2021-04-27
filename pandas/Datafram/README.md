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
















