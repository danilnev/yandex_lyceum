commands = []
n = int(input())
for i in range(n):
    name = input()
    mark = int(input())
    commands.append((name, mark))
flag1 = (n // 2) + (n % 2)
result = []

for i in range(flag1):
    maxx = 0
    for j in range(len(commands)):
        if commands[j][1] > maxx:
            index = j
            maxx = commands[j][1]
    result.append(commands[index])
    del commands[index]

for i in range(len(result)):
    index = 0
    for j in range(1, len(result)):
        if result[j][0] < result[index][0]:
            index = j
    print(result[index][0])
    del result[index]

for i in range(len(commands)):
    index = 0
    for j in range(1, len(commands)):
        if commands[j][0] < commands[index][0]:
            index = j
    print(commands[index][0])
    del commands[index]
