def move_wrap(canvas, obj, move):
    canvas.move(obj, move[0], move[1])
    x = canvas.coords(obj)[0]
    y = canvas.coords(obj)[1]
    if x > 600:
        x = 0
    if y > 600:
        y = 0
    canvas.move(obj, x, y)
