import tkinter


def key_pressed(event):
    if event.keysym == 'space':
        canvas.coords(oval, (300, 300, 310, 310))
    elif event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    elif event.keysym == 'Down':
        canvas.move(oval, 0, 10)
    elif event.keysym == 'Right':
        canvas.move(oval, 10, 0)
    elif event.keysym == 'Left':
        canvas.move(oval, -10, 0)
    if abs(canvas.coords(oval)[1] - 305) >= 100 or abs(canvas.coords(oval) [0] - 305) >= 100:
        canvas.itemconfig(oval, fill='red')
    else:
        canvas.itemconfig(oval, fill='green')


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='green')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
