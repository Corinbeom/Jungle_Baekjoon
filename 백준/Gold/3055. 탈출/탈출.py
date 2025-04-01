from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

tmap = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(R):
    layer = (input().strip())
    
    tmap.append(list(layer))

water_q = deque()
gosm_q = deque()

visited = [[False] * C for _ in range(R)] 

for y in range(R):
    for x in range(C):
        if tmap[y][x] == "*":
            water_q.append((y, x))
        elif tmap[y][x] == "S":
            gosm_q.append((y, x))
            visited[y][x] = True  


time = 0

while gosm_q:
    
    for _ in range(len(water_q)):
        wy, wx = water_q.popleft()
       
        for i in range(4):
            nwy = wy + dy[i]
            nwx = wx + dx[i]
           
            if 0 <= nwx < C and 0 <= nwy < R and tmap[nwy][nwx] == '.':
                tmap[nwy][nwx] = '*'
                water_q.append((nwy, nwx))
    for _ in range(len(gosm_q)):
        y, x = gosm_q.popleft()
        
        
        if tmap[y][x] == 'D':
            print(time) 
            exit()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
                
            if 0 <= nx < C and 0 <= ny < R:
                if tmap[ny][nx] == 'D':
                    print(time + 1) 
                    exit()
                if tmap[ny][nx] == '.' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    gosm_q.append((ny, nx))
    time += 1
                
print("KAKTUS")
