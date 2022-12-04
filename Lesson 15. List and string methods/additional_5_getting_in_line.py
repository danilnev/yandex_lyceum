num_events = int(input())
line = []
for i in range(num_events):
    event = input()
    if event.endswith('в очередь.'):
        index = event.find(' встал')
        line.append(event[:index])
    elif event.startswith('Привет'):
        index1 = event.split('! ')[1].find(' будет')
        people = event.split('! ')[1][:index1]
        above = event.split('! ')[0][8:]
        index2 = line.index(above)
        line.insert(index2 + 1, people)
    else:
        line.remove(event.split(', ')[0])
print('\n'.join(line))
