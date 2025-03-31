import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().strip())) for _ in range(N)]

dist = [[float('inf')] * N for _ in range(N)]
dist[0][0] = 0 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()
dq.append((0,0))

while dq:
    x, y = dq.popleft()
    cur_cost = dist[x][y]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        
        if graph[nx][ny] == 1:
            total_cost = cur_cost
            if total_cost < dist[nx][ny]:
                dist[nx][ny] = total_cost
                dq.appendleft((nx,ny))
        else:
            total_cost = cur_cost + 1
            if total_cost < dist[nx][ny]:
                dist[nx][ny] = total_cost
                dq.append((nx, ny))
                
print(dist[N-1][N-1])