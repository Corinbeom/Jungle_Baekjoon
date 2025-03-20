n = int(input())
nums = []

for i in range(n):
    num = int(input())
    nums.append(num)

nums.sort()

for j in range(len(nums)):
    print(nums[j])