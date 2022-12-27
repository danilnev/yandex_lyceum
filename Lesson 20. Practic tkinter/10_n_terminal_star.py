import tkinter
import math

master = tkinter.Tk()
canvas = tkinter.Canvas(master, height=200, width=200)
last_crd = (100, 100)
num = int(input())
for i in range(num):
    crd1 = math.cos(2 * 3 * i / num) + 100
    crd2 = math.sin(2 * 3 * i / num) + 100
    canvas.create_line(last_crd, crd1, crd2, fill='red')
    last_crd = (crd1, crd2)
canvas.pack()
master.mainloop()
