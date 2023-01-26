def count_food(days):
    summ = 0
    for day in days:
        summ += daily_food[day - 1]
    return summ


# daily_food = [0, 150, 150]
# print(count_food([2, 3]))
