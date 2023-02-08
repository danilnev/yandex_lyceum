import math

R = 1
min_s = None
point = (0, 75)
numbers = []
i = 0
while i <= math.pi * 2:
    numbers.append(i)
    i += 0.01
for t in numbers:
    x = R * math.cos(t)
    y = R * math.sin(t)
    s = math.sqrt((x - point[0]) ** 2 + (y - point[1]) ** 2)
    if not min_s or s < min_s:
        min_s = s
print(min_s)
