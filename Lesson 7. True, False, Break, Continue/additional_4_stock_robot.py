last_day = int(input())
buy = 0
sell = 0
while True:
    price = int(input())
    if price == 0:
        break
    else:
        if buy == 0 and price > last_day:
            buy = price
        elif sell == 0 and price < last_day and buy != 0:
            sell = price
        last_day = price
print(buy, sell, sell - buy)