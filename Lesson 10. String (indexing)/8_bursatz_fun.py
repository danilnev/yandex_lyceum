n = int(input())
while n < 1000000000 and str(n)[0] != '1':
    n *= int(str(n)[0])
print(n)
