n = int(input())

nums = list(map(int, input().split()))

cnt = 0

for x in nums:
  for i in range(2, x+1):
    if x % i == 0:
      if x == i:
        cnt += 1
      
      break

print(cnt)