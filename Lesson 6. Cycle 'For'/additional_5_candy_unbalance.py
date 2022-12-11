candies = int(input())
minn_candies = candies
for i in range(1, candies + 1):
    summ_i = sum([j for j in range(1, i + 1)])
    if (candies - summ_i) % i == 0:
        minn_candies = candies - summ_i // i
print(minn_candies)
