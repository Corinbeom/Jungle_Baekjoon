N = int(input())

stack = []

for i in range(N):
    nums = int(input())
    
    if nums == 0:
        stack.pop()
    else:
        stack.append(nums)
    
print(sum(stack))