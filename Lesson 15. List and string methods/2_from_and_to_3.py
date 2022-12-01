numbers = [int(num) ** 2 for num in input().split()]
m, k = input().split()
print(sum(numbers[int(m):int(k) + 1]))
