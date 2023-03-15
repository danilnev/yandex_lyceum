num = int(input())
names = list()
nums = list()
for i in range(num):
    names.append(input())
    nums.append(int(input()))
for i in range(num - 1, -1, -1):
    print(names[i], nums[i])