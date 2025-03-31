from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    
visited = [-1] * (N + 1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    
    while queue:
        now = queue.popleft()
        for next_city in graph[now]:
            if visited[next_city] == -1:
                visited[next_city] = visited[now] + 1
                queue.append(next_city)
                

bfs(X)

for i in range(1, N+1):
    if visited[i] == K:
        print(i)
        
if K not in visited:
    print(-1)
    
