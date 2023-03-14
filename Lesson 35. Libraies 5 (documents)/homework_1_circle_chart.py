import xlsxwriter
import sys

doc = xlsxwriter.Workbook('res.xlsx')
sheet = doc.add_worksheet()
data = list(map(lambda x: (x.split()[0], int(x.split()[1])), sys.stdin.readlines()))
for row, (item, price) in enumerate(data):
    sheet.write(row, 0, item)
    sheet.write(row, 1, price)
chart = doc.add_chart({'type': 'pie'})
chart.add_series({'values': '=Sheet1!B1:B5', 'categories': '=Sheet1!A1:A5'})
sheet.insert_chart('C3', chart)
doc.close()
