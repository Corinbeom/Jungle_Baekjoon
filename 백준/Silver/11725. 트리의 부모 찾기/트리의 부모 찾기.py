import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

parent = [0] * (N+1)

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

def dfs(node):
    visited[node] = True
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            parent[neighbor] = node
            dfs(neighbor)
        
dfs(1)

for i in range(2, N+1):
    print(parent[i])


