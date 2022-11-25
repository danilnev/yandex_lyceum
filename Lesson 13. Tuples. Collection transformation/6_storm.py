num = int(input())
places = []
for i in range(num):
    height = int(input())
    iron = float(input())
    places.append((height, iron))
for i in range(num):
    for j in range(num):
        if places[i][0] == places[j][0] and places[i][1] > places[j][1]:
            places[i], places[j] = places[j], places[i]
        elif places[i][0] > places[j][0]:
            places[i], places[j] = places[j], places[i]
for place in places:
    print(place)