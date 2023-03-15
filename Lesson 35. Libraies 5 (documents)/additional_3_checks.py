import xlsxwriter


def export_check(text):
    doc = xlsxwriter.Workbook('res.xlsx')
    text = text.split('---')
    text = list(map(lambda x: x.split('\n'), text))
    text = list(map(lambda x: list(map(lambda y: y.split('\t'), x)), text))
    text = list(map(lambda x: list(filter(lambda y: y[0], x)), text))
    text = list(map(lambda x: list(map(lambda y: [y[0], int(y[1]), int(y[2])], x)), text))
    for check in text:
        sheet = doc.add_worksheet()
        for i, p in enumerate(check):
            if p[:2] in map(lambda x: x[:2], check[:i]):
                check[list(map(lambda x: x[:2], check[:i])).index(p[:2])][2] += p[2]
                check[i][2] = 0
        check = list(filter(lambda x: x[2] != 0, check))
        check.sort(key=lambda x: x[0])
        for i, string in enumerate(check):
            sheet.write(i, 0, string[0])
            sheet.write(i, 1, string[1])
            sheet.write(i, 2, string[2])
            sheet.write(i, 3, f'=B{i + 1}*C{i + 1}')
        sheet.write(len(check), 0, 'Итого')
        sheet.write(len(check), 3, f'=SUM(D1:D{len(check)})')
    doc.close()


export_check(
    'товар 1\t100\t5\nтовар 2\t200\t6\nтовар 3\t7\t500\nтовар 1\t100\t5\nтовар 2\t200\t6\nтовар 3\t7\t500\n---\nтовар '
    '1\t100\t5\nтовар 2\t200\t6\nтовар 3\t7\t500\nтовар 1\t100\t5\nтовар 2\t200\t6\nтовар 3\t7\t500\nтовар '
    '1\t100\t5\nтовар 2\t200\t6\nтовар 3\t7	500\n')
