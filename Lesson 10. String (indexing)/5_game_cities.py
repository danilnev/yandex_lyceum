last_city = input()
while True:
    city = input()
    if last_city[-1] == city[0]:
        last_city = city
        continue
    else:
        print(city)
        break
