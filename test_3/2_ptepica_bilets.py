import datetime


date1, date2 = map(lambda x: datetime.date(*list(map(int, x.split('-')))),
                   input().split())
n = int(input())
dates = []
while date1 <= date2:
    if date1.day % n != 0 and date1.weekday() != 1:
        dates.append(date1.strftime('%d %B %Y, %a'))
    date1 += datetime.timedelta(days=1)
if len(dates) < 3:
    print('CANCEL CARNIVAL')
else:
    print(*dates[:3], sep='\n')
