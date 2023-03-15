m = int(input())
already_cook = set()
for i in range(m):
    already_cook.add(input())
days = int(input())
for i in range(days):
    num = int(input())
    for i in range(num):
        already_cook.discard(input())
for elem in already_cook:
    print(elem)