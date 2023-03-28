friends = dict()
keys = []
values = []
num = int(input())
for i in range(num):
    keys.append(input())
string = input()
while string != '':
    values.append(string)
    string = input()
for key in keys:
    for value in values:
        if len(value) >= len(key) and len(set(value.lower()).intersection(set(key.lower()))) > 0:
            friends[key.lower()] = value.upper()
            break
print('{')
for key in friends.keys():
    print(f'\t"{key}": "{friends[key]}",')
print('}')
