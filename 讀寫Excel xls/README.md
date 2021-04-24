# 讀寫Excel xls 檔


## 讀取Excel
```python 

import xlrd
path = r"test.xls"

#get workbook
workbook = xlrd.open_workbook(path)

#get sheet_names
workbook.sheet_names()

#get worksheet by name
worksheet = workbook.sheet_by_name("test1")

#get worksheet by index
worksheet = workbook.sheet_by_name("test1"

#get cell value row = 2 col = 3 (start from 0)
worksheet.cell_value(1,2) 

# get max row
worksheet.nrows

# get max column
worksheet.ncols

)


```















