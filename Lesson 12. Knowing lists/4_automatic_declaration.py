num1 = int(input())
parts = list()
for i in range(num1):
    parts.append(input())
num2 = int(input())
for i in range(num2):
    print(parts[int(input()) - 1])