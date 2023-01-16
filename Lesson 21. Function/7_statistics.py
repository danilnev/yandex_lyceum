def print_statistics(arr):
    if len(arr) == 0:
        print('\n'.join(['0' for i in range(5)]))
    else:
        arr.sort()
        if len(arr) % 2 == 0:
            median = (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2
        else:
            median = arr[len(arr) // 2]
        print(len(arr), sum(arr) / len(arr), float(min(arr)), float(max(arr)), float(median), sep='\n')


# print_statistics([])
# print_statistics([22])
# print_statistics([1, 54, 2, 66, 107, 8])
# print_statistics([90, 91])
