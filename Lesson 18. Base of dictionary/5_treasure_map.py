num = int(input())
places = []
count = 0
for i in range(num):
    crds = input().split()
    crd1 = crds[0]
    crd2 = crds[1]
    places.append([crd1, crd2])
for i in range(num):
    num1_i = places[i][0][0]
    num2_i = places[i][1][0]
    for j in range(num):
        if places[i] != places[j]:
            num1_j = places[j][0][0]
            num2_j = places[j][1][0]
            if num1_i == num1_j and num2_i == num2_j:
                count += 1
print(count)
