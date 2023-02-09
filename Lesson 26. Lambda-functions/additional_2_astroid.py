import math

R = 1
min_s = 100
point = (0.75, 0)
numbers = []
i = 0
while i <= math.pi * 2:
    numbers.append(i)
    i += 1 * (10 ** -4)
for t in numbers:
    x = R * (math.cos(t) ** 3)
    y = R * (math.sin(t) ** 3)
    s = math.sqrt((x - point[0]) ** 2 + (y - point[1]) ** 2)
    if s < min_s:
        min_s = s
print(round(min_s, 4))
