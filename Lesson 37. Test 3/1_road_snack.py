import random


products = input().split()
num_r = tuple(map(int, input().split()))
weight_r = tuple(map(float, input().split()))
for i, el in enumerate(random.sample(products, 3), 1):
    weight = round(random.uniform(*weight_r), 1)
    num = random.randint(*num_r)
    print(f'{i}. {el} weighing {weight} kg, {num} of pieces, {round(weight * num, 1)} kg.')
