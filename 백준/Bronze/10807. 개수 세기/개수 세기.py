n = int(input())

arr = list(map(int, input().split()))

m = int(input())

count = 0

for i in range(len(arr)):
    if arr[i] == m:
        count += 1

print(count)