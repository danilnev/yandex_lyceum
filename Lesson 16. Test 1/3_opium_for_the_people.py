num = int(input())
first = set()
second = set()
for i in range(num):
    string1 = input().split()
    string2 = input().split()
    first = first.union(string1)
    second = second.union(string2)
print(' '.join(first.intersection(second)))
