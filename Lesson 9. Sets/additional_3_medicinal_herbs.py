num_of_medicines = int(input())
needs_prods = set()
for i in range(num_of_medicines):
    num_of_ingredients = int(input())
    for i in range(num_of_ingredients):
        needs_prods.add(input())
for elem in needs_prods:
    print(elem)
