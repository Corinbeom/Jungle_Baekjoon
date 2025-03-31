from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maze = []

for _ in range(N):
    a = list(map(int, input().strip()))
    
    maze.append(a)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx,ny))
                    
bfs(0,0)
print(maze[N-1][M-1])