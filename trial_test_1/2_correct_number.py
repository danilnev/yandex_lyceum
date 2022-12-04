strings = [len(input()) for i in range(3)]
step = min(strings)
strings.remove(step)
begin = max(strings)
strings.remove(begin)
end = strings[0]
numbers = []
for i in range(begin, end, -step):
    numbers.append(str(i))
print(' '.join(numbers))
