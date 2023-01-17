def equation(a, b):
    crd1_x = float(a.split(';')[0])
    crd1_y = float(a.split(';')[1])
    crd2_x = float(b.split(';')[0])
    crd2_y = float(b.split(';')[1])
    if crd1_y == crd2_y:
        print(crd1_y)
    elif crd1_x == crd2_x:
        print(crd1_x)
    else:
        k = (crd1_y - crd2_y) / (crd1_x - crd2_x)
        b = crd2_y - k * crd2_x
        print(k, b)


# equation("0;0", "1;1")
# equation("0;0", "0;4")
# equation("4;6.9", "-5.2;6.9")
