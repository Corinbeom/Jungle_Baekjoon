import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

A = input().strip()
is_inside = [False] + [c == '1' for c in A]

graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0

def dfs(node):
    visited[node] = True
    count = 0
    
    for neighbor in graph[node]:
        if is_inside[neighbor]:
            count += 1
        elif not visited[neighbor]:
            count += dfs(neighbor)
    return count

counted = set()
for i in range(1, N+1):
    for j in graph[i]:
        if is_inside[i] and is_inside[j]:
            key = tuple(sorted((i, j)))
            if key not in counted:
                counted.add(key)
            result += 1
    
for i in range(1, N+1):
    if not visited[i] and not is_inside[i]:
        k = dfs(i)
        result += k * (k - 1)
        
print(result)