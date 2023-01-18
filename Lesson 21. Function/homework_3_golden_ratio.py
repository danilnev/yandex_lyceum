def golden_ratio(i):
    fibonachi = [1, 1]
    for j in range(2, i + 1):
        fibonachi.append(fibonachi[j - 1] + fibonachi[j - 2])
    print(fibonachi[i] / fibonachi[i - 1])


# golden_ratio(10)
# golden_ratio(2)
# golden_ratio(4)
