def quarter(xcoord, ycoord):
    if xcoord > 0 and ycoord > 0:
        print('I четверть')
    elif xcoord > 0 and ycoord < 0:
        print('IV четверть')
    elif xcoord < 0 and ycoord < 0:
        print('III четверть')
    else:
        print('II четверть')


# quarter(3, 4)
# quarter(-3.5, 8)
