# Dataframe


<a href = "https://pandas.pydata.org/pandas-docs/stable/reference/frame.html">官方連結</a>
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
map  = {
        "subject": subject,  
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

## Attributes and underlying data

<ul>
    <li>shape</li>
    <li>describe()</li>  
    <li>columns</li>
    <li>index</li>
    <li>empty</li>
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


## 讀取外部資料
<ul>
    <li>read csv</li>
    <li>read html</li>
    <li>read excel</li> 
</ul>

## read_csv

```
>>> pd.read_csv(path)
     #                   Player  GP   MIN   PTS   FGM   FGA   FG%  ...  OREB  DREB   REB   AST  STL  BLK  TOV   EFF
0    1             James Harden  61  36.7  34.4   9.9  22.7  43.5  ...   1.0   5.3   6.4   7.4  1.7  0.9  4.5  31.8
1    2             Bradley Beal  57  36.0  30.5  10.4  22.9  45.5  ...   0.9   3.3   4.2   6.1  1.2  0.4  3.4  25.4
2    3    Giannis Antetokounmpo  57  30.9  29.6  10.9  20.0  54.7  ...   2.3  11.5  13.7   5.8  1.0  1.0  3.7  34.8
3    4               Trae Young  60  35.3  29.6   9.1  20.8  43.7  ...   0.5   3.7   4.3   9.3  1.1  0.1  4.8  26.6
4    5           Damian Lillard  58  36.9  28.9   9.2  20.0  45.7  ...   0.5   3.8   4.3   7.8  1.0  0.4  2.9  27.8
5    6              Luka Doncic  54  33.3  28.7   9.5  20.6  46.1  ...   1.3   8.0   9.3   8.7  1.1  0.2  4.2  30.4
6    7        Russell Westbrook  53  35.9  27.5  10.7  22.6  47.4  ...   1.8   6.3   8.0   7.0  1.7  0.3  4.5  26.7
7    8            Kawhi Leonard  51  32.2  26.9   9.3  19.9  46.9  ...   1.0   6.3   7.3   5.0  1.8  0.6  2.7  27.5
8    9            Anthony Davis  55  34.3  26.7   9.2  18.1  51.1  ...   2.3   7.1   9.4   3.1  1.5  2.4  2.5  30.5
9   10             Devin Booker  62  36.1  26.1   8.8  18.0  48.7  ...   0.4   3.7   4.2   6.6  0.7  0.3  3.9  24.0
10  11             LeBron James  60  34.9  25.7   9.8  19.6  49.8  ...   1.0   6.9   7.9  10.6  1.2  0.5  4.0  30.4
.......


```

## read_excel
```
xl= pd.ExcelFile(path)
sheet_name = xl.sheet_names[0]
df = xl.parse(sheet_name,header)

```




## 資料選取

### DataFrame.head(n)

取出前五項(default n = 5)
```
>>> df.head()
   #                 Player  GP   MIN   PTS   FGM   FGA   FG%  3PM   3PA   3P%   FTM   FTA   FT%  OREB  DREB   REB  AST  STL  BLK  TOV   EFF
0  1           James Harden  61  36.7  34.4   9.9  22.7  43.5  4.4  12.6  35.2  10.1  11.8  86.1   1.0   5.3   6.4  7.4  1.7  0.9  4.5  31.8
1  2           Bradley Beal  57  36.0  30.5  10.4  22.9  45.5  3.0   8.4  35.3   6.8   8.0  84.2   0.9   3.3   4.2  6.1  1.2  0.4  3.4  25.4
2  3  Giannis Antetokounmpo  57  30.9  29.6  10.9  20.0  54.7  1.5   4.8  30.6   6.3  10.0  63.3   2.3  11.5  13.7  5.8  1.0  1.0  3.7  34.8
3  4             Trae Young  60  35.3  29.6   9.1  20.8  43.7  3.4   9.5  36.1   8.0   9.3  86.0   0.5   3.7   4.3  9.3  1.1  0.1  4.8  26.6
4  5         Damian Lillard  58  36.9  28.9   9.2  20.0  45.7  3.9   9.9  39.4   6.7   7.6  88.8   0.5   3.8   4.3  7.8  1.0  0.4  2.9  27.8
```

### DataFrame.tail(n)
取出後五項(
```
>>> df.tail(3)
     #           Player  GP   MIN   PTS  FGM   FGA   FG%  3PM  3PA   3P%  FTM  FTA   FT%  OREB  DREB  REB  AST  STL  BLK  TOV   EFF
47  48  Devonte' Graham  63  35.1  18.2  5.8  15.3  38.2  3.5  9.3  37.3  3.0  3.7  82.0   0.7   2.7  3.4  7.5  1.0  0.2  2.9  17.3
48  49     Derrick Rose  50  26.0  18.1  7.4  15.1  49.0  0.9  2.9  30.6  2.4  2.8  87.1   0.5   1.9  2.4  5.6  0.8  0.3  2.5  16.6
49  50     Terry Rozier  63  34.4  18.0  6.3  14.9  42.3  2.7  6.7  40.7  2.6  3.0  87.4   0.8   3.6  4.4  4.1  1.0  0.2  2.2  16.4
>>>
```


### df['col_name'] or df[['col_name1','col_name2']]

```
>>> df['Name']
>>> df['Player']
0                James Harden
1                Bradley Beal
2       Giannis Antetokounmpo
3                  Trae Young
4              Damian Lillard
5                 Luka Doncic
6           Russell Westbrook
7               Kawhi Leonard
8               Anthony Davis
9                Devin Booker
10               LeBron James
...
Name: Player, dtype: object
```

```
>>> df[['Player','PTS']][:10]
                  Player   PTS
0           James Harden  34.4
1           Bradley Beal  30.5
2  Giannis Antetokounmpo  29.6
3             Trae Young  29.6
4         Damian Lillard  28.9
5            Luka Doncic  28.7
6      Russell Westbrook  27.5
7          Kawhi Leonard  26.9
8          Anthony Davis  26.7
9           Devin Booker  26.1
>>>
```

### df.iloc

#### df.iloc[row]
列出第三筆資料
```
>>> df.iloc[2]
#                             3
Player    Giannis Antetokounmpo
GP                           57
MIN                        30.9
PTS                        29.6
FGM                        10.9
FGA                          20
FG%                        54.7
3PM                         1.5
3PA                         4.8
3P%                        30.6
FTM                         6.3
FTA                          10
FT%                        63.3
OREB                        2.3
DREB                       11.5
REB                        13.7
AST                         5.8
STL                           1
BLK                           1
TOV                         3.7
EFF                        34.8
Name: 2, dtype: object
```
#### df.iloc[row][col]
列出第三筆資料的第二欄
```
>>> df.iloc[2][1]
'Giannis Antetokounmpo'
```

#### df.iloc[[row_indexs],[col_indexs]]
```
>>> df.iloc[[1,3,5]]
   #        Player  GP   MIN   PTS   FGM   FGA   FG%  3PM  3PA   3P%  FTM  FTA   FT%  OREB  DREB  REB  AST  STL  BLK  TOV   EFF
1  2  Bradley Beal  57  36.0  30.5  10.4  22.9  45.5  3.0  8.4  35.3  6.8  8.0  84.2   0.9   3.3  4.2  6.1  1.2  0.4  3.4  25.4
3  4    Trae Young  60  35.3  29.6   9.1  20.8  43.7  3.4  9.5  36.1  8.0  9.3  86.0   0.5   3.7  4.3  9.3  1.1  0.1  4.8  26.6
5  6   Luka Doncic  54  33.3  28.7   9.5  20.6  46.1  2.9  9.1  31.8  6.8  9.1  75.2   1.3   8.0  9.3  8.7  1.1  0.2  4.2  30.4
>>> df.iloc[[1,3,5],[1,2,3,4]]
         Player  GP   MIN   PTS
1  Bradley Beal  57  36.0  30.5
3    Trae Young  60  35.3  29.6
5   Luka Doncic  54  33.3  28.7
```


#### df.iloc 切片
```
>>> df.iloc[:2,0:4]
   #        Player  GP   MIN
0  1  James Harden  61  36.7
1  2  Bradley Beal  57  36.0    50       40       80       50
```


#### df.loc[row_index]/df.loc[row_index][col_name]
用法跟df.iloc 類似但是使用名稱
```
>>> df.loc[0]
>>> df.loc[0]
#                    1
Player    James Harden
GP                  61
MIN               36.7
PTS               34.4
FGM                9.9
FGA               22.7
FG%               43.5
3PM                4.4
3PA               12.6
3P%               35.2
FTM               10.1
FTA               11.8
FT%               86.1
OREB                 1
DREB               5.3
REB                6.4
AST                7.4
STL                1.7
BLK                0.9
TOV                4.5
EFF               31.8
Name: 0, dtype: object
>>>

>>> df.loc[:][["Player","GP"]][:10]
                  Player  GP
0           James Harden  61
1           Bradley Beal  57
2  Giannis Antetokounmpo  57
3             Trae Young  60
4         Damian Lillard  58
5            Luka Doncic  54
6      Russell Westbrook  53
7          Kawhi Leonard  51
8          Anthony Davis  55
9           Devin Booker  62
>>>

```

## DataFrame 資料filter
使用方法df [條件]
### 一般使用
```
>>> df[(df["EFF"] > 30) & (df["PTS"] > 28)]
   #                 Player  GP   MIN   PTS   FGM   FGA   FG%  3PM   3PA   3P%   FTM   FTA   FT%  OREB  DREB   REB  AST  STL  BLK  TOV   EFF
0  1           James Harden  61  36.7  34.4   9.9  22.7  43.5  4.4  12.6  35.2  10.1  11.8  86.1   1.0   5.3   6.4  7.4  1.7  0.9  4.5  31.8
2  3  Giannis Antetokounmpo  57  30.9  29.6  10.9  20.0  54.7  1.5   4.8  30.6   6.3  10.0  63.3   2.3  11.5  13.7  5.8  1.0  1.0  3.7  34.8
5  6            Luka Doncic  54  33.3  28.7   9.5  20.6  46.1  2.9   9.1  31.8   6.8   9.1  75.2   1.3   8.0   9.3  8.7  1.1  0.2  4.2  30.4
>>>
```

### 使用lambda

```
>>> df[ lambda x : x.EFF >30]
     #                 Player  GP   MIN   PTS   FGM   FGA   FG%  3PM   3PA   3P%   FTM   FTA   FT%  OREB  DREB   REB   AST  STL  BLK  TOV   EFF
0    1           James Harden  61  36.7  34.4   9.9  22.7  43.5  4.4  12.6  35.2  10.1  11.8  86.1   1.0   5.3   6.4   7.4  1.7  0.9  4.5  31.8
2    3  Giannis Antetokounmpo  57  30.9  29.6  10.9  20.0  54.7  1.5   4.8  30.6   6.3  10.0  63.3   2.3  11.5  13.7   5.8  1.0  1.0  3.7  34.8
5    6            Luka Doncic  54  33.3  28.7   9.5  20.6  46.1  2.9   9.1  31.8   6.8   9.1  75.2   1.3   8.0   9.3   8.7  1.1  0.2  4.2  30.4
8    9          Anthony Davis  55  34.3  26.7   9.2  18.1  51.1  1.2   3.5  33.5   7.0   8.3  84.5   2.3   7.1   9.4   3.1  1.5  2.4  2.5  30.5
10  11           LeBron James  60  34.9  25.7   9.8  19.6  49.8  2.2   6.4  34.9   4.0   5.7  69.7   1.0   6.9   7.9  10.6  1.2  0.5  4.0  30.4
```

篩選多個
```
>>> df[ (lambda x : x.EFF >30) and (lambda x : x.PTS >28)]
   #                 Player  GP   MIN   PTS   FGM   FGA   FG%  ...  OREB  DREB   REB  AST  STL  BLK  TOV   EFF
0  1           James Harden  61  36.7  34.4   9.9  22.7  43.5  ...   1.0   5.3   6.4  7.4  1.7  0.9  4.5  31.8
1  2           Bradley Beal  57  36.0  30.5  10.4  22.9  45.5  ...   0.9   3.3   4.2  6.1  1.2  0.4  3.4  25.4
2  3  Giannis Antetokounmpo  57  30.9  29.6  10.9  20.0  54.7  ...   2.3  11.5  13.7  5.8  1.0  1.0  3.7  34.8
3  4             Trae Young  60  35.3  29.6   9.1  20.8  43.7  ...   0.5   3.7   4.3  9.3  1.1  0.1  4.8  26.6
4  5         Damian Lillard  58  36.9  28.9   9.2  20.0  45.7  ...   0.5   3.8   4.3  7.8  1.0  0.4  2.9  27.8
5  6            Luka Doncic  54  33.3  28.7   9.5  20.6  46.1  ...   1.3   8.0   9.3  8.7  1.1  0.2  4.2  30.4

```

搭配使用apply
```
>>> df[ df.apply(lambda x : x['EFF'] >30,axis = 1)]
     #                 Player  GP   MIN   PTS   FGM   FGA   FG%  ...  OREB  DREB   REB   AST  STL  BLK  TOV   EFF
0    1           James Harden  61  36.7  34.4   9.9  22.7  43.5  ...   1.0   5.3   6.4   7.4  1.7  0.9  4.5  31.8
2    3  Giannis Antetokounmpo  57  30.9  29.6  10.9  20.0  54.7  ...   2.3  11.5  13.7   5.8  1.0  1.0  3.7  34.8
5    6            Luka Doncic  54  33.3  28.7   9.5  20.6  46.1  ...   1.3   8.0   9.3   8.7  1.1  0.2  4.2  30.4
8    9          Anthony Davis  55  34.3  26.7   9.2  18.1  51.1  ...   2.3   7.1   9.4   3.1  1.5  2.4  2.5  30.5
10  11           LeBron James  60  34.9  25.7   9.8  19.6  49.8  ...   1.0   6.9   7.9  10.6  1.2  0.5  4.0  30.4

[5 rows x 22 columns]
>>>
```


### 搭配DataSeries

<ul>
    <li>df[col_name].isin(array)</li>
    <li>df[col_name].str.contains(str, na=False)  </li>
    <li>df[col_name].lt (lt/le/gt/ge/eq)</li>  
</ul>



### df[col_name].str.contains(str, na=False)  
```
>>> filter = df["Player"].str.contains("James", na=False)
>>> df[filter]
     #        Player  GP   MIN   PTS  FGM   FGA   F
0    1  James Harden  61  36.7  34.4  9.9  22.7  43
10  11  LeBron James  60  34.9  25.7  9.8  19.6  49
```


### df[col_name].lt (lt,le,gt,ge,eq)
也可以使用df.col_name 方式
```
>>> filter_EFF = df["EFF"].gt(30)
>>> filter_PTS = df.PTS.gt(28)
>>> df[filter_EFF & filter_PTS]
   #                 Player  GP   MIN   PTS   FGM   FGA   FG%  3PM   3PA   3P%   FTM   FTA   FT%  OREB  DREB   REB  AST  STL  BLK  TOV   EFF
0  1           James Harden  61  36.7  34.4   9.9  22.7  43.5  4.4  12.6  35.2  10.1  11.8  86.1   1.0   5.3   6.4  7.4  1.7  0.9  4.5  31.8
2  3  Giannis Antetokounmpo  57  30.9  29.6  10.9  20.0  54.7  1.5   4.8  30.6   6.3  10.0  63.3   2.3  11.5  13.7  5.8  1.0  1.0  3.7  34.8
5  6            Luka Doncic  54  33.3  28.7   9.5  20.6  46.1  2.9   9.1  31.8   6.8   9.1  75.2   1.3   8.0   9.3  8.7  1.1  0.2  4.2  30.4
```

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
















