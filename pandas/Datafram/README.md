# Dataframe


<a href = "https://pandas.pydata.org/pandas-docs/stable/reference/frame.html">官方連結</a>


<ul>
    <li><a href = "https://nbviewer.jupyter.org/github/Eddie02582/Python/blob/master/pandas/Datafram/Create%20data%20and%20Basic%20operation.ipynb">Create data and Basic operation</a></li>
    <li><a href = "https://nbviewer.jupyter.org/github/Eddie02582/Python/blob/master/pandas/Datafram/Read%20data%20and%20Data%20selection.ipynb">Read data and Data selection</a></li>
    <li><a href = "https://nbviewer.jupyter.org/github/Eddie02582/Python/blob/master/pandas/Datafram/Data%20Filter.ipynb">Data Filter</a></li>
    <li><a href = "https://nbviewer.jupyter.org/github/Eddie02582/Python/blob/master/pandas/Datafram/Data%20Filter.ipynb">Combine Data</a></li>
</ul>


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
















