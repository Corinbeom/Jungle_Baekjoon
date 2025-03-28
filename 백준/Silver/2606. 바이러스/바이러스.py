import sys
input = sys.stdin.readline

N = int(input())

C = int(input())

com_pair = [[] for _ in range(N+1)]

for _ in range(C):
    a, b = map(int, input().split())
    
    com_pair[a].append(b)
    com_pair[b].append(a)
    
visited = [False] * (N + 1)

def dfs(node):
    visited[node] = True
    
    for neighbor in com_pair[node]:
        if not visited[neighbor]:
            dfs(neighbor)
            
dfs(1)
print(sum(visited) -1)