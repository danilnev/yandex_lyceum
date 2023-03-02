import datetime as dt


days = int(input())
now_date = dt.datetime.now()
date = now_date + dt.timedelta(days=days)
print(date.day, date.month)
