n,m = map(int, input().split())

bucket = [(i)+1 for i in range(n)]
tmp = 0

arr = [(list(map(int, input().split()))) for _ in range(m)]

for k in range(m):
    tmp = bucket[arr[k][0]-1]
    bucket[arr[k][0]-1] = bucket[arr[k][1]-1]
    bucket[arr[k][1]-1] = tmp
    
for j in bucket:
    print(j, end=' ')