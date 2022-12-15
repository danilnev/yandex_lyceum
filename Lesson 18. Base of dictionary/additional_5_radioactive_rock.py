string = input().split()
rocks = dict()
i = 0
while i < len(string):
    name = string[i]
    count = string[i + 1]
    rocks[name] = count
    i += 2
print(rocks)
