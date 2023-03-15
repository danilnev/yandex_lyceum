summ = 0
count = 0
while True:
    num = int(input())
    count += 1
    summ += num
    if summ == 10:
        print(count)
        break