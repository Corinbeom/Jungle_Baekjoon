import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

needs = [[0] * (N + 1) for _ in range(N + 1)]

in_degree = [0] * (N + 1)

queue = deque()

result = []

for _ in range(M):
    a, b, c = map(int, input().split())
    
    graph[b].append((a,c))
    in_degree[a] += 1
    
for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)
        needs[i][i] = 1

while queue:
    now = queue.popleft()
    result.append(now)
    
    for next, _ in graph[now]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            queue.append(next)
            
for now in result:
    for next, count in graph[now]:
        for i in range(1, N+1):
            needs[next][i] += needs[now][i] * count
            
for i in range(1,N+1):
    if needs[N][i] > 0:
        print(i, needs[N][i])