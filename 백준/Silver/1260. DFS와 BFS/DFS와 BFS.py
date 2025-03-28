import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)
    
for adj in graph:
    adj.sort()
    
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

def dfs(node):
    visited_dfs[node] = True
    print(node, end=" ")
    
    for next in graph[node]:
        if visited_dfs[next] == False:
            dfs(next)
            
def bfs(start, graph, visited_bfs):
    queue = deque([start])
    visited_bfs[start] = True
    
    while queue:
        current = queue.popleft()
        print(current, end=" ")
    
        for next in graph[current]:
            if visited_bfs[next] == False:
                queue.append(next)
                visited_bfs[next] = True
            
dfs(V)
print()
bfs(V, graph, visited_bfs)