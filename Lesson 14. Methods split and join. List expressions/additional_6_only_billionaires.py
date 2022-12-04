journals = [number.split(',') for number in input().split(';')]
sums = [[summ for summ in journal if int(summ) >= 1000000000] for journal in journals]
strings = [','.join(summ) for summ in sums]
print('\n'.join(strings))
