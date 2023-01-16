def equationa(a, b):
    crd1_x = a.split(';')[0]
    crd1_y = a.split(';')[1]
    crd2_x = b.split(';')[0]
    crd2_y = b.split(';')[1]
    if crd1_x == crd2_x:
        print(crd1_x)
    elif crd1_y == crd2_y:
        print(crd1_y)