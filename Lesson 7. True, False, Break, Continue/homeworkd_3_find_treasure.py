x = int(input())
y = int(input())
xx = 0
yy = 0
count = 0

while xx != x or yy != y:
    orient = input()
    if orient == 'стоп':
        break
    num = int(input())
    count += 1
    if orient == 'север':
        yy += num
    elif orient == 'восток':
        xx += num
    elif orient == 'юг':
        yy -= num
    else:
        xx -= num
    if x == xx and y == yy:
        break
print(count)