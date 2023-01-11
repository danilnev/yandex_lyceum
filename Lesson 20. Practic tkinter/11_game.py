import tkinter
import random


def prepare_and_start():
    global player, exit, fires, enemies
    canvas.delete('all')
    player_pos = (random.randint(0, N_X - 1) * step,
                  random.randint(0, N_Y - 1) * step)
    exit_pos = (random.randint(0, N_X - 1) * step,
                random.randint(0, N_Y - 1) * step)
    player = canvas.create_image(player_pos,
                                 image=player_pic, anchor='nw')
    exit = canvas.create_image(exit_pos,
                               image=exit_pic, anchor='nw')
    N_FIRES = 6
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(0, N_X - 1) * step,
                    random.randint(0, N_Y - 1) * step)
        fire = canvas.create_image(fire_pos,
                                   image=fire_pic, anchor='nw')
        fires.append(fire)
    N_ENEMIES = 4
    enemies = []
    for i in range(N_ENEMIES):
        enemy_pos = (random.randint(0, N_X - 1) * step,
                     random.randint(0, N_Y - 1) * step)
        enemy = canvas.create_image(enemy_pos,
                                    image=enemy_pic, anchor='nw')
        enemies.append((enemy, random.choice([always_right, random_move])))
    label.config(text='Найти выход:')
    label.pack()
    canvas.pack()
    master.bind("<KeyPress>", key_pressed)


def always_right():
    return (step, 0)


def random_move():
    return random.choice([(step, 0), (-step, 0), (0, step), (0, -step)])


def do_nothing(x):
    pass


def move_wrap(obj, move):
    canvas.move(obj, move[0], move[1])
    if canvas.coords(player)[0] > 599:
        canvas.move(player, -600, 0)
    elif canvas.coords(player)[1] > 599:
        canvas.move(player, 0, -600)
    elif canvas.coords(player)[0] < 0:
        canvas.move(player, 600, 0)
    elif canvas.coords(player)[1] < 0:
        canvas.move(player, 0, 600)


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")
        master.bind('<KeyPress>', do_nothing)
    for fire in fires:
        if canvas.coords(player) == canvas.coords(fire):
            label.config(text='Ты проиграл!')
            master.bind('<KeyPress>', do_nothing)
    for enemy in enemies:
        if canvas.coords(enemy[0]) == canvas.coords(player):
            label.config(text='Ты проиграл!')
            master.bind('<KeyPress>', do_nothing)


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, (0, -step))
    elif event.keysym == 'Down':
        move_wrap(player, (0, step))
    elif event.keysym == 'Right':
        move_wrap(player, (step, 0))
    elif event.keysym == 'Left':
        move_wrap(player, (-step, 0))
    for enemy in enemies:
        move = enemy[1]()
        move_wrap(enemy[0], move)
    check_move()


master = tkinter.Tk()
step = 60
N_X = 10
N_Y = 10
player_pic = tkinter.PhotoImage(file='images/player_pic.gif')
exit_pic = tkinter.PhotoImage(file='images/exit_pic.gif')
fire_pic = tkinter.PhotoImage(file='images/fire_pic.gif')
enemy_pic = tkinter.PhotoImage(file='images/enemy_pic.gif')
label = tkinter.Label(master, text='Найди выход')
label.pack()
canvas = tkinter.Canvas(master, bg='blue', height=N_X * step, width=N_Y * step)
canvas.pack()
restart = tkinter.Button(master, text='Начать заново', command=prepare_and_start)
restart.pack()
prepare_and_start()
master.mainloop()
