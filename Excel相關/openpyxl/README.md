# openpyxl 

<a href ="https://openpyxl.readthedocs.io/en/stable/index.html">官網教學</a>

## install 

```
    pip install openpyxl
```


## 架構
操作分二部分
<ul>
    <li>workbook</li>
    <li>sheet</li>  
</ul>

## How to Manipulate workbook


### create workbook

```python
from openpyxl import Workbook
wb = Workbook()
wb.save("sample.xlsx")
```

### read exist workbook

```python
from openpyxl import load_workbook
wb = load_workbook('data.xlsx')
wb.save("sample.xlsx")
```


### get workbook sheets

```python
print (wb.sheetnames)
```

### get create sheets
loc為要插入的位置
```python
sheet = wb.create_sheet(sheet_name,loc)
```



## How to Manipulate sheet

首先要先取得sheet,有兩種方法
<ul>
    <li>get sheet by name:sheet = wb[sheet_name]</li>
    <li>get sheet by index:sheet = wb[wb.sheetnames[index]]</li>
    <li>利用切片</li>
</ul>

### write value
以下方式皆可寫值

```python
sheet.cell(1,1).value = "A1"
sheet["A1"].value = "A1"
sheet.cell(row =1, column = 1,value = "A1")
sheet.cell(row =1, column = 1).value = "A1"
```

### read value
以下方式皆可寫值

```python
sheet.cell(1,1).value
sheet["A1"].value 
sheet.cell(row =1, column = 1).value = "A1"
```

### get sheet max row
```python
sheet.max_row
```

### get sheet max column
```python
sheet.max_column
```

### set column width 

```python
sheet.column_dimensions["A1"].width = width 
```

### set Alignment 

```python
from openpyxl.styles import  Alignment
alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)    
sheet["A2"].alignment = alignment   
```



### set sheet projection

```python
sheet.protection.sheet = True
sheet.protection.password  = password
```
如果需要取消
```python
sheet.protection.password  =password
sheet.protection.sheet = False  
```

### set partial protection 

```python
sheet.cell(row = 1,column = 1).protection = Protection(locked=False)     
```
       
## Inserting and deleting rows and columns
<ul>
    <li>Worksheet.insert_rows()</li>
    <li>Worksheet.insert_cols()</li>
    <li>Worksheet.delete_rows()</li>
    <li>Worksheet.delete_cols()</li>
</ul>
在第七row插入一行空的
```python
sheet.insert_rows(7)
```
在第6 column開始再刪3columns(6,7,8)
```python
sheet.delete_cols(6, 3)
```

## Moving ranges of cells
```python
sheet.move_range("A24:R27", rows=-1, cols=2)
```

## Read large Data

```python
from openpyxl import load_workbook
wb = load_workbook(filename='large_file.xlsx', read_only=True)
ws = wb['big_data']

for row in ws.rows:
    for cell in row:
        print(cell.value)

# Close the workbook after reading
wb.close()
```








