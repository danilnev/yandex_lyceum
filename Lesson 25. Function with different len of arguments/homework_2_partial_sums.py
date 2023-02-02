def partial_sums(*args):
    if not args:
        return [0]
    numbers = [0, args[0]]
    count = 2
    while True:
        summ = 0
        if count <= len(args):
            summ += sum([args[i] for i in range(count)])
            count += 1
            numbers.append(summ)
        else:
            break
    return numbers


# print(partial_sums(13))
# print(partial_sums(1, 0.5, 0.25, 0.125))
# print(partial_sums())
