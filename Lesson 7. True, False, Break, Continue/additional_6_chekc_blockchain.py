n = int(input())
result = -1
last_h = 0
for i in range(n):
    bc = int(input())
    h = bc % 256  # bn = hn + rn×256 + mn×2562
    r = (bc % (256**2)) // 256
    m = bc // (256**2)
    if h > 100 or h != ((m + r + last_h) * 37) % 256:  # hn = 37×(mn+rn+hn-1)
        result = i
        break
    last_h = h
print(result)