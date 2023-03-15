maxx = int(input())
num = int(input())
for i in range(num):
    name = input()
    if len(name) > maxx:
        print(name[:maxx - 3] + '...')
    else:
        print(name)