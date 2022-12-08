rows = int(input())
triangle = [['1']]
for i in range(1, rows):
    last_row = triangle[i - 1]
    row = ['1']
    for j in range(len(last_row) - 1):
        row.append(str(int(last_row[j]) + int(last_row[j + 1])))
    row.append('1')
    triangle.append(row)
print('\n'.join(['\t'.join(row) for row in triangle]))
