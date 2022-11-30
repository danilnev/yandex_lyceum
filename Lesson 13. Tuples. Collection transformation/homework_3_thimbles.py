num_thimbles = int(input())
last_thimbles = [input() for i in range(num_thimbles)]
num_transformation = int(input())
for i in range(num_transformation):
    number = int(input())
    thimbles = []
    for j in range(number):
        index = int(input())
        thimbles.append(last_thimbles[index - 1])
    last_thimbles = thimbles
for thimble in thimbles:
    print(thimble)
