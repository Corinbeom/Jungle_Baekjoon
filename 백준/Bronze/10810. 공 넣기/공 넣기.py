n, m = map(int, input().split())

arr = [(list(map(int, input().split()))) for _ in range(m)]

result = [0] * (n + 1)

for i in range(m):
    for k in range(arr[i][0], arr[i][1] + 1):
        result[k] = arr[i][2]

for i in range(1, n + 1):
    print(result[i], end=' ')