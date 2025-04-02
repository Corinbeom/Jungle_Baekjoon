'''
탐색하면서 field[y][x] 가 1 이면 주변 방문 OK 만들고 주변에 1을 찾으며 주변 1이 다 방문을 했거나 0이면 지나온 거리를 덩어리로 만들기
시작 노드는 field[0][0]
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

field = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0

apt_list = []

def dfs(y, x, visited):
    global count
    visited[y][x] = True
    count += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N:
            if field[ny][nx] == 1 and visited[ny][nx] == False:
                dfs(ny, nx, visited)
                


for y in range(N):
    for x in range(N):
        if field[y][x] == 1 and not visited[y][x]:
            count = 0
            dfs(y, x, visited)
            apt_list.append(count)


print(len(apt_list))
apt_list = sorted(apt_list)

for i in range(len(apt_list)):
    print(apt_list[i])
