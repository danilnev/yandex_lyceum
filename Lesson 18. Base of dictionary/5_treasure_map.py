num = int(input())
places = []
lengths = dict()
for i in range(num):
    crds = input().split()
    crd1 = crds[0]
    crd2 = crds[1]
    places.append((crd1, crd2))
for i in range(num):
    num1_i = places[i][0][:-1]
    num2_i = places[i][1][:-1]
    if (num1_i, num2_i) not in lengths:
        array = [(num1_i, num2_i)]
        for j in range(num):
            if i != j:
                num1_j = places[j][0][:-1]
                num2_j = places[j][1][:-1]
                if num1_i == num1_j and num2_i == num2_j:
                    array.append((num1_j, num2_j))
        lengths[(num1_i, num2_i)] = len(array)
print(max(lengths.values()))
