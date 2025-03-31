import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C = map(int,input().split())

ice_berg = []

for _ in range(R):
    ice_colum = list(map(int, input().split()))
    ice_berg.append(ice_colum)
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def melt_iceberg(ice_berg, R, C):
    next_ice = [row[:] for row in ice_berg]
    
    for r in range(R):
        for c in range(C):
            if ice_berg[r][c] > 0:
                water_count = 0
                for i in range(4):
                    nr = r + dx[i]
                    nc = c + dy[i]
                    
                    if 0 <= nr < R and 0 <= nc < C:
                        if ice_berg[nr][nc] == 0:
                            water_count += 1
                            
                next_ice[r][c] = max(0, ice_berg[r][c] - water_count)
                
    return next_ice

def count_iceberg(ice_berg, R, C):
    visited = [[False] * C for _ in range(R)]
    count = 0
    
    for r in range(R):
        for c in range(C):
            if ice_berg[r][c] > 0 and not visited[r][c]:
                dfs(r, c, visited, ice_berg)
                count += 1
    return count

def dfs(r,c,visited,ice_berg):
    visited[r][c] = True
    
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        
        if 0 <= nr < R and 0 <= nc < C:
            if ice_berg[nr][nc] > 0 and not visited[nr][nc]:
                dfs(nr,nc,visited,ice_berg)

year = 0
while True:
    cnt = count_iceberg(ice_berg, R, C)

    if cnt == 0:
        print(0)
        break
    elif cnt >= 2:
        print(year)
        break

    ice_berg = melt_iceberg(ice_berg, R, C)  
    year += 1
