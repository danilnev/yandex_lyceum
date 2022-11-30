s = int(input())
brothers = [[], []]
for i in range(s):
    value = int(input())
    brothers[0].append(value)
    brothers[1].append(value)
n = int(input())
for i in range(n):
    num_brother = int(input())
    value = int(input())
    summ = int(input())
    brothers[num_brother - 1][value] += summ
count = 0
for i in range(s):
    if brothers[0][i] == brothers[1][i]:
        count += 1
for brother in brothers:
    string = str(brother[0])
    for i in range(1, s):
        string += ' ' + str(brother[i])
    print(string)
print(count)
