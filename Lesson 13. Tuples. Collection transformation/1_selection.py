num = int(input())
students = []
for i in range(num):
    students.append(input())
for elem in students:
    print(elem)
print()
for elem in students:
    if 4 <= int(elem[-1]) <= 5:
        print(elem)