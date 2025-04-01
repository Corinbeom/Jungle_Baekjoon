import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

indegree = [0] * (N+1)

Q = deque()

result = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


for i in range(1, N+1):
    if indegree[i] == 0:
        Q.append(i)

while Q:
    now = Q.popleft()
    result.append(now)
    
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            Q.append(next)
            
print(*result)