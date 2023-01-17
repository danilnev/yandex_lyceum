def line(s, t):
    k = float(s.split('x')[0])
    b = float(s.split('x')[1][1:])
    x = float(t.split(';')[0])
    y = float(t.split(';')[1])
    if (y == k * x + b and s.split('x')[1][0] == '+') or (y == k * x - b and s.split('x')[1][0] == '-'):
        print('True')
    else:
        print('False')


# line("1x+6", "1;7")
# line("5x-10", "5;-9")
# line("0x+7", "3;7")
# line("-0.24x-9.4", "8.6;-11.464")
