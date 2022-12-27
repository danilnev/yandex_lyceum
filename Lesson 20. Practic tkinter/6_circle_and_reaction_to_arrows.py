import tkinter


def key_pressed(event):
    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    elif event.keysym == 'Down':
        canvas.move(oval, 0, 10)
    elif event.keysym == 'Right':
        canvas.move(oval, 10, 0)
    elif event.keysym == 'Left':
        canvas.move(oval, -10, 0)


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='red')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
