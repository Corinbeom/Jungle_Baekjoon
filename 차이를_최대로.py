from itertools import permutations

n = int(input())

arr = list(map(int, input().split()))


perm = permutations(arr)

max_value = 0


for p in perm:
    total = sum(abs(p[i] - p[i + 1]) for i in range(n - 1))
    max_value = max(max_value, total)


print(max_value)



