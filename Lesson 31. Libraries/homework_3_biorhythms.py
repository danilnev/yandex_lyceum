import datetime
import math


p = [23, 28, 33]
birth_date = list(map(int, input().split('.')))
birth_date = datetime.date(*reversed(birth_date))
now_date = list(map(int, input().split('.')))
now_date = datetime.date(*reversed(now_date))
t = (now_date - birth_date)
t = t.days
for period in p:
    print('%.2f' % (math.sin((2 * math.pi * t) / period) * 100))
