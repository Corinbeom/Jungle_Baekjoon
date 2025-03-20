def find_area(n, hi, rh, visited):
    from collections import deque
    
    # 4방향 이동 (상, 하, 좌, 우)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]    
    
    def bfs(x,y):
        queue = deque([(x,y)])  #  시작 위치를 큐에 넣음
        visited[x][y] = True    #  방문 표시 (중복 방문 방지)
        
        while queue:            #  큐가 빌 떄 까지 반복
            cx, cy = queue.popleft()        #  큐에서 원소 하나 꺼내서
            for i in range(4):              #  4방향(상하좌우) 확인
                nx, ny = cx + dx[i], cy + dy[i]

                # 1) 지도 범위 안에 있는지 확인 (0 <= nx < n and 0 <= ny < n)
                # 2) 해당 위치가 비의 높이(rh)보다 높은지 확인 (hi[nx][ny] > rh)
                #    -> 비의 높이보다 낮거나 같으면 물에 잠겼으니 제외
                # 3) 아직 방문하지 않은 곳인지 (not visited[nx][ny])
                if 0 <= nx < n and 0 <= ny < n and hi[nx][ny] > rh and not visited[nx][ny]:
                    visited[nx][ny] = True  # 방문 처리
                    queue.append((nx, ny))  # 큐에 넣어 BFS 계속 진행

    safe_area_count = 0  # 현재 비 높이 rh에서, 안전 영역(덩어리)이 몇 개인지 저장
    
    for i in range(n):   # 지도 전체를 돌면서
        for j in range(n):
            # hi[i][j]가 rh보다 커야 '안전(물에 잠기지 않음)' 상태고,
            # 방문 안 했으면 새로운 안전 영역 하나 발견한 것
            if hi[i][j] > rh and not visited[i][j]:  # 물에 잠기지 않은 새로운 영역 발견
                bfs(i, j)             # 그 지점부터 BFS로 연결된 안전 구역을 전부 탐색
                safe_area_count += 1  # 새로운 구역 하나 찾았으니 개수 +1

    return safe_area_count  # 이 높이(rh)에서의 안전 영역 개수 반환




n = int(input())  # 지도 크기 (NxN)

# (HeightInfo)2차원 배열에 높이 정보 저장
hi = [list(map(int, input().split())) for _ in range(n)]  

# (RainHeight)비의 최대 높이 설정 (입력된 높이 중 가장 큰 값)
rh = max(map(max, hi))

max_safe_areas = 1  # 최소 1개의 안전 영역 존재

for h in range(rh + 1):  # 모든 비 높이에 대해 탐색
    visited = [[False] * n for _ in range(n)]  # 방문 리스트 초기화
    max_safe_areas = max(max_safe_areas, find_area(n, hi, h, visited))  # 최댓값 갱신

print(max_safe_areas)  # 최댓값 출력

