import random
import sys


peoples1 = list(map(str.rstrip, sys.stdin))
peoples2 = peoples1.copy()
result = []
for p in peoples1:
    people = random.choice(peoples2)
    while people == p:
        people = random.choice(peoples2)
    print(f'{p} - {people}')
    peoples2.remove(people)
