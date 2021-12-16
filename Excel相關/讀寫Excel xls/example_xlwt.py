from xlwt import Workbook, XFStyle, Borders, Pattern, Font,Formula,Alignment
from datetime import date

workbook = Workbook(encoding = 'utf-8')

#add_sheet(sheetname, cell_overwrite_ok=False)
worksheet = workbook.add_sheet('My Worksheet',cell_overwrite_ok = True)

#worksheet.write(r,c,label,style)
# write row = 0 ,col = 0 ,label = 'A'
worksheet.write(0,0,'A')
worksheet.write(0,1,'B')
worksheet.write(0,2,'A * B')


#worksheet.write(r,c,label,style)
#worksheet.row(r).write(c,label,style)


for row in range(1,5):   
    # get specific row 
    row1 = worksheet.row(row)
    row1.write(0,row)
    row1.write(1,row)
    # 設定公式
    formula = "A{0}*B{0}".format(row + 1)
    worksheet.write(row,2, Formula(formula))
    

# 設定單元格寬度
worksheet.col(0).width = 256 *10
worksheet.col(1).width = 256 *10

# 設定row 高度
worksheet.row(0).height_mismatch = True
worksheet.row(0).height = 256 *10


#新增一個超連結
worksheet.write(0, 3, Formula('HYPERLINK("http://www.google.com";"Google")'))

#Merge r1, r2, c1, c2 
#merge row 2 col 3-4
worksheet.write_merge(2, 3,2, 4, 'Merge') 

# 初始化樣式
style = XFStyle() 

#設定文字樣式
font = Font()
font.name = 'Times New Roman'
font.bold = True
font.underline = True
font.italic = True
style.font = font


#設定邊框
borders = Borders()
# DASHED ,NO_LINE,THIN
borders.left = Borders.DASHED
borders.right = Borders.DASHED
borders.top = Borders.THICK
borders.bottom = Borders.THICK
borders.left_colour = 0x40
borders.right_colour = 0x40
style.borders = borders


# 為單元格設定背景色:
pattern = Pattern()
pattern.pattern = Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 0x0A
style.pattern = pattern

style.num_format_str='YYYY-MM-DD'


# Alignment
alignment = Alignment()
alignment.horz = Alignment.HORZ_CENTER
alignment.vert = Alignment.VERT_CENTER
style.alignment = alignment

worksheet.col(4).width = 256 *30
#write value with style
worksheet.write(0,4,date(2009,3,18),style)
workbook.save('example.xls')







