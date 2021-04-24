# 讀寫Excel xls 檔


## 讀取Excel

```
	pip install xlrd
```

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

## 寫入Excel

```
	pip install xlwt
```


```python 

import xlwt
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet')

# write value 5 to excel row = 0,col = 0 
worksheet.write(0,0,5)

# write value 2 to excel row = 0,col = 1
worksheet.write(0, 1,2 )

# 設定單元格寬度
worksheet.col(0).width = 100


# 設定公式
worksheet.write(1, 0, xlwt.Formula('A1*B1'))
worksheet.write(1, 1, xlwt.Formula('SUM(A1,B1)'))

#新增一個超連結
worksheet.write(0, 3, xlwt.Formula('HYPERLINK("http://www.google.com";"Google")'))

#Merge r1, r2, c1, c2 
#merge row 2 col 3-4
worksheet.write_merge(2, 2, 3, 4, 'Merge') 


# 初始化樣式
style = xlwt.XFStyle() 

#設定文字樣式
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
font.underline = True
font.italic = True

style.font = font


#設定邊框
borders = xlwt.Borders()
# DASHED ,NO_LINE,THIN
borders.left = xlwt.Borders.DASHED
borders.right = xlwt.Borders.DASHED
borders.left_color = 0x40

style.borders = borders

# 為單元格設定背景色:
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN 
style.pattern = pattern_fore_colour = 5
worksheet.write(5, 2, 'Style', style)
workbook.save('Excel_Style.xls')
```











