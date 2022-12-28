import math
import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=200, width=200)
pi = 3.14
num = int(input())
for i in range(num):
    if num % 2 == 0:
        i1 = (i + (num / 2) - 1) % num
    else:
        i1 = (i + (num - 1) / 2) % num
    crd1 = math.cos((2 * pi * i) / num) * 50 + 100, math.sin((2 * pi * i) / num) * 50 + 100
    crd2 = math.cos((2 * pi * i1) / num) * 50 + 100, math.sin((2 * pi * i1) / num) * 50 + 100
    canvas.create_line(crd1, crd2, fill='black')
canvas.pack()
master.mainloop()
