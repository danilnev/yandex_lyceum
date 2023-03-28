num = int(input())
numbers = []
for i in range(num):
    numbers.append([int(number) for number in input().split(';')])
search = int(input())
letters = list(str(search))
for array in numbers:
    array.sort(reverse=True)
    flag = True
    for number in array:
        flag1 = True
        if number % search == 0:
            flag2 = True
            for let in str(number):
                if let in letters:
                    flag2 = False
                    break
            if not flag2:
                flag1 = False
        else:
            flag1 = False
        if flag1:
            print(number)
            flag = False
            break
    if flag:
        print()
