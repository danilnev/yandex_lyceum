height = int(input())
width = int(input())
picture = [0] * height
for i in range(height):
    picture[i] = input()
for i in range(0, height, 2):
    string = ''
    for j in range(0, width, 2):
        string += picture[i][j]
    print(string)
