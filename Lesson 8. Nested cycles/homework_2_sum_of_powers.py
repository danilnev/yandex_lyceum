num = int(input())
result_sum = 0
for i in range(1, num + 1):
    summ = 0
    for j in range(1, i + 1):
        if j % 2 == i % 2:
            summ += j
    result_sum += i ** summ
print(result_sum)