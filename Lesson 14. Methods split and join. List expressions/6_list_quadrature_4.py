print(' '.join([str(int(number) ** 2) for number in input().split()
                if int(number) % 2 == 1 and int(number) ** 2 % 10 != 9]))