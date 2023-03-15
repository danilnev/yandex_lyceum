num = int(input())
nums = list()
for i in range(num):
    nums.append(int(input()))
beg = int(input())
fin = int(input())
summ = 0
for i in range(beg - 1, fin):
    summ += nums[i]
print(summ)