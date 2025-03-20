from itertools import*

N, M = map(int, input().split())

arr = []

for i in range(1, N+1):
    arr.append(i)
    
nnr = combinations(arr, M)

nar = list(nnr)

for i in range(len(nar)):
    print(*nar[i])