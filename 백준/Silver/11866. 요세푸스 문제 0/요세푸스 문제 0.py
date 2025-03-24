import sys

N, K = map(int, sys.stdin.readline().split())

arr = []

delete_arr = []

for i in range(1, N+1):
    arr.append(i)
    
idx = 0

while arr:
    idx = (idx + K - 1) % len(arr)
    removed = arr.pop(idx)
    delete_arr.append(removed)
    
print("<" + ", ".join(map(str, delete_arr)) + ">")