import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, -1, -1,  0, 0, 1, 1, 1]
dy = [-1,  0,  1, -1, 1, -1, 0, 1]


def dfs(x, y, map_p, visited):
    visited[x][y] = True
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if map_p[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny, map_p, visited)

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    map_p = [list(map(int, input().split())) for _ in range(h)]
    
    visited = [[False]*w for _ in range(h)]
    
    count = 0
    
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and map_p[i][j] == 1:
                dfs(i, j, map_p, visited)
                count += 1
    print(count)
