from itertools import*

N, M = map(int, input().split())

arr = []

for i in range(1, N+1):
    arr.append(i)
    
nrr = permutations(arr, M)

res_arr = list(nrr)

for j in range(len(res_arr)):
    print(*res_arr[j])