from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

box = []
for _ in range(H):
    layer = []
    for _ in range(N):
        layer.append(list(map(int, input().split())))
    box.append(layer)
    
queue = deque()

for z in range(0, H):
    for y in range(0, N):
        for x in range(0, M):
            if box[z][y][x] == 1:
                queue.append((x,y,z))
                
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while queue:
    x, y, z = queue.popleft()
    
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                queue.append((nx, ny, nz))
                
max_day =0

for z in range(0, H):
    for y in range(0, N):
        for x in range(0, M):
            if box[z][y][x] == 0:
                print(-1)
                exit()
            max_day = max(max_day, box[z][y][x])
            
print(max_day - 1)