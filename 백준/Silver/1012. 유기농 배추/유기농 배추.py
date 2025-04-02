import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

TC = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y, visited, field, M, N):
    visited[y][x] = True
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < M and 0 <= ny < N:
            if not visited[ny][nx] and field[ny][nx] == 1:
                dfs(nx, ny, visited, field, M, N)


for _ in range(TC):
    
    M, N, K = map(int, input().split())
    visited = [[False] * M for _ in range(N)]
    field = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    count = 0
    
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:
                dfs(x, y, visited, field, M, N)
                count += 1
                
    print(count)