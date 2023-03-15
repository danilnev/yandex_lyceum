side = float(input())
speed = float(input())
count = 0
if side < 1 or speed > side:
    print(count)
else:
    while abs(side - speed) > 0.01:
        side = (speed ** 2 + (side - speed) ** 2) ** 0.5
        count += 1
    print(count)