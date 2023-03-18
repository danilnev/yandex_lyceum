import numpy as np


table = np.genfromtxt('ABBREV.csv', delimiter=';', dtype=None, names=True, encoding="utf8")
best_call = []
maxx_call = 0
best_good = []
minn_good = None
best_prote = []
maxx_prote = 0
vitamin = ()

for product in table:
    if product[3] > maxx_call:
        best_call.clear()
        best_call.append(product[1])
        maxx_call = product[3]
    elif product[3] == maxx_call:
        best_call.append(product[1])

    if minn_good is None or product[9] < minn_good:
        best_good.clear()
        best_good.append(product[1])
        minn_good = product[9]
    elif product[9] == minn_good:
        best_good.append(product[1])

    if product[4] > maxx_prote:
        best_prote.clear()
        best_prote.append(product[1])
        maxx_prote = product[4]
    elif product[4] == maxx_prote:
        best_prote.append(product[1])

    if vitamin == () or product[20] > vitamin[1]:
        vitamin = (product[1], product[20])

print(best_call[-1])
print(best_good[0])
print(best_prote[-1])
print(vitamin[0])
