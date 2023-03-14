from docxtpl import DocxTemplate


def create_training_sheet(class_name, subject_name, tpl_name='tpl.docx', *args):
    marks = []
    args = sorted(args, key=lambda x: x[0])
    for arg in args:
        name = arg[0]
        number = list(map(lambda x: x[0], args)).index(name) + 1
        mark = arg[1]
        marks.append({
            'num': number,
            'fio': name,
            'mark': mark
        })
    data = {
        'class_name': class_name,
        'subject_name': subject_name,
        'marks': marks
    }
    doc = DocxTemplate(tpl_name)
    doc.render(data)
    doc.save('res.docx')


# create_training_sheet("3И", "Математика", "tpl.docx",
#                       ("Петров Петр", "5"),
#                       ("Иванов Иван", "5"),
#                       ("Сергеев Сергей", "3"),
#                       ("Никитин Никита", "4"))
