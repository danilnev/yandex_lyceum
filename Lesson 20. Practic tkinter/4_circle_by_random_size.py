import tkinter
import random

def draw(event):
    coords = []
    for i in range(4):
        coords.append(random.randint(0, 600))
    canvas.create_oval((coords[0], coords[1]), (coords[2], coords[3]), fill='red')
    return


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()
