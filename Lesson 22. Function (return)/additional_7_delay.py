def islower(time1, time2):
    h1 = int(time1.split(':')[0])
    m1 = int(time1.split(':')[1])
    h2 = int(time2.split(':')[0])
    m2 = int(time2.split(':')[1])
    if h1 < h2:
        return True
    elif h1 == h2 and m1 <= m2:
        return True
    else:
        return False


def time_plus_time(time1, time2):
    h1 = int(time1.split(':')[0])
    m1 = int(time1.split(':')[1])
    h2 = int(time2.split(':')[0])
    m2 = int(time2.split(':')[1])
    h = h1 + h2 + ((m1 + m2) // 60)
    m = (m1 + m2) % 60
    return f'{h}:{m}'


def time_minus_time(time1, time2):
    h1 = int(time1.split(':')[0])
    m1 = int(time1.split(':')[1])
    h2 = int(time2.split(':')[0])
    m2 = int(time2.split(':')[1])
    h = h1 - h2
    m = m1 - m2
    if m < 0:
        h -= 1
        m = 60 - abs(m)
    return f'{h}:{m}'


def late(now: str, classes: str, buses: list[int]):
    buses.sort(reverse=True)
    for bus in buses:
        mins = time_plus_time(f'00:{bus}', '00:15')
        time = time_plus_time(now, mins)
        if islower(time, classes) and bus >= 5:
            return f'Выйти через {bus - 5} минут'
    return 'Опоздание'


# print(late('12:00', '12:40', [0, 1, 4, 6, 25]))
# print(late('9:20', '9:35', [4, 25, 30]))
# print(late('13:50', '14:30', [7, 17, 35, 48]))
