today = input()
clear = float(input())
cloudy = float(input())
days = int(input())
prob = 1
for i in range(days):
    if today == 'ясно':
        if clear > 1 - clear:
            today = 'ясно'
            prob *= clear
        elif clear < 1 - clear:
            today = 'пасмурно'
            prob *= 1 - p
