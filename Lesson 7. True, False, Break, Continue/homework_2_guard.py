while True:
    num = int(input())
    if num == 0:
        break
    elif num % 7 == 0 and num % 3 == 0:
        print('Караул!')
        break
    elif num % 3 == 0:
        print('несчастливое')
    elif num % 7 == 0:
        print('опасное')
    else:
        print(num)