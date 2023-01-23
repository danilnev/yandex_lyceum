import tkinter


def move_wrap(obj, move):
    canvas.move(obj, move[0], move[1])
    x = canvas.coords(obj)[0]
    y = canvas.coords(obj)[1]
    if x >= 600:
        x = 1
        canvas.coords(obj, x, y, x + 10, y + 10)
    if y >= 600:
        y = 1
        canvas.coords(obj, x, y, x + 10, y + 10)


def key_pressed(event):
    if event.keysym == 'space':
        canvas.coords(oval, (300, 300, 310, 310))
    elif event.keysym == 'Up':
        move_wrap(oval, (0, -10))
    elif event.keysym == 'Down':
        move_wrap(oval, (0, 10))
    elif event.keysym == 'Right':
        move_wrap(oval, (10, 0))
    elif event.keysym == 'Left':
        move_wrap(oval, (-10, 0))
    if abs(canvas.coords(oval)[1] - 305) >= 100 or abs(canvas.coords(oval)[0] - 305) >= 100:
        canvas.itemconfig(oval, fill='red')
    else:
        canvas.itemconfig(oval, fill='green')


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='green')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
