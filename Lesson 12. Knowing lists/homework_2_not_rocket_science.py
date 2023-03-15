num = int(input())
nums = list()
for i in range(num):
    nums.append(int(input()))
for i in range(num - 1):
    print(nums[i] + nums[i + 1])