n, m = map(int, input().split())

bucket = [i for i in range(1,n+1)]

tmp = 0

for x in range(m):
    i,j = map(int, input().split())
    tmp = bucket[i-1:j]
    tmp.reverse()
    bucket[i-1:j] = tmp
    
for x in range(n):
    print(bucket[x], end=" ")