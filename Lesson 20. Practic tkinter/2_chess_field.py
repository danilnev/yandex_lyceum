import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
for i in range(75, 600, 75):
    canvas.create_line((i, 0), (i, 600), fill='black')
    canvas.create_line((0, i), (600, i), fill='black')
begin = 0
for i in range(0, 151, 75):
    for j in range(begin * 75, 526, 150):
            canvas.create_oval((j, i), (j + 75, i + 75), fill='red')
    if begin == 0:
        begin = 1
    else:
        begin = 0
for i in range(375, 526, 75):
    for j in range(begin * 75, 526, 150):
            canvas.create_oval((j, i), (j + 75, i + 75), fill='blue')
    if begin == 0:
        begin = 1
    else:
        begin = 0
canvas.pack()
master.mainloop()
