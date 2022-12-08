indexes = [int(num) for num in input().split()]
words = input().split()
print(' '.join([words[index - 1].lower() for index in indexes]).capitalize())
