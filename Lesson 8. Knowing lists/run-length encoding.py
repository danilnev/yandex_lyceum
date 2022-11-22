string = input()
listt = list()
listt.extend(string)
i = 0
while i < len(listt):
    count = 0
    symbol = listt[i]
    while string[i] == symbol:
        i += 1
        count += 1
        if i >= len(listt):
            break
    print(count, symbol)
