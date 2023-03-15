m = int(input())
products = set()
for i in range(m):
    products.add(input())
n = int(input())
for i in range(n):
    name = input()
    ingredients = set()
    num = int(input())
    for i in range(num):
        ingredients.add(input())
    if products >= ingredients:
        print(name)