import xlsxwriter


def export_check(text):
    text = list(map(lambda x: x.split('\t'), text.split('\n')))
    text = list(map(lambda x: [x[0], int(x[1]), int(x[2])], text))
    doc = xlsxwriter.Workbook('res.xlsx')
    sheet = doc.add_worksheet()
    for i, string in enumerate(text):
        sheet.write(i, 0, string[0])
        sheet.write(i, 1, string[1])
        sheet.write(i, 2, string[2])
        sheet.write(i, 3, f'=Sheet1!B{i + 1}*C{i + 1}')
    sheet.write(len(text), 0, 'Итого')
    sheet.write(len(text), 3, f'=SUM(D1:D{len(text)})')
    doc.close()


# export_check('продукты\t2\t50\nфрукт\t3\t20\nцветок\t6\t30\nсметана\t10\t40')
