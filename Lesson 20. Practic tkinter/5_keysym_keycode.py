import tkinter


def show_key(event):
    label.config(text=f'''keysym - {event.keysym}
char - {event.char}
keysum_num - {event.keysym_num}
keycode - {event.keycode}''')


master = tkinter.Tk()
label = tkinter.Label(master, text="Hello world!")
label.pack()
master.bind("<KeyPress>", show_key)
master.mainloop()
