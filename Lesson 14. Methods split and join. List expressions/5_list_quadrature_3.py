numbers = input().split()
squad_numbers = [str(int(number) ** 2) for number in numbers]
print(' '.join(squad_numbers))