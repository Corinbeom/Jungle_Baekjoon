import sys
from collections import deque
input = sys.stdin.readline

# 바이러스가 퍼질 맵 크기(N)와 바이러스 종류 수(K) 입력
N, K = map(int, input().split())

virus_map = []  # 시험관 상태 (N x N)
virus_point = []  # 바이러스 위치 정보 저장할 배열 (바이러스 번호, 행, 열)

# 바이러스 맵 초기 상태 입력받기 및 바이러스 위치 저장
for r in range(N):
    row = list(map(int, input().split()))
    virus_map.append(row)
    
    for c in range(N):
        if row[c] != 0:
            virus_point.append((row[c], r, c))  # (바이러스 번호, 행, 열)

# S초 뒤에 목표위치(x,y)에 존재하는 바이러스 출력하기 위한 입력 받기
S, target_x, target_y = map(int, input().split())

# 작은 번호부터 먼저 퍼지기 때문에 오름차순 정렬
virus_point.sort()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 큐 초기화 (바이러스 번호, 행, 열, 시간)
queue = deque()
for virus_num, r, c in virus_point:
    queue.append((virus_num, r, c, 0))

# BFS 실행
while queue:
    virus_num, x, y, time = queue.popleft()

    # S초가 된다면 탈출 
    if time == S:
        break
    
    # 상하좌우로 바이러스 전파 시도
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 맵 범위 안이고,   
        if 0 <= nx < N and 0 <= ny < N:
            if virus_map[nx][ny] == 0:  # 아직 바이러스가 퍼지지 않은 칸이면
                virus_map[nx][ny] = virus_num  # 바이러스 전파
                queue.append((virus_num, nx, ny, time + 1))  # 다음 시간에 전파될 위치

# S초 뒤에 목표위치에 존재하는 바이러스 번호 출력
print(virus_map[target_x - 1][target_y - 1])