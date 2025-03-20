from itertools import permutations  # 순열을 생성하기 위해 permutations 사용

n = int(input())  # 도시의 수 입력받기

# 비용 행렬 입력 (N x N)
w = [list(map(int, input().split())) for _ in range(n)]

min_cost = float('inf')  # 최소 비용을 무한대로 초기화

cities = range(n)  # 도시 번호 (0부터 n-1까지)

# 모든 방문 순서(순열) 생성
all_paths = permutations(cities)

for path in all_paths:  # 모든 순열(경로)을 확인
    current_cost = 0  # 현재 경로의 비용
    valid = True  # 유효한 경로인지 체크
    
    # 경로를 따라가면서 비용 계산
    for i in range(n - 1):
        if w[path[i]][path[i + 1]] == 0:  # 두 도시 간 길이 없으면 중단
            valid = False
            break
        current_cost += w[path[i]][path[i + 1]]  # 비용 누적

        if current_cost >= min_cost:  # 현재 비용이 최소 비용보다 크면 더 볼 필요 없이 중단
            valid = False
            break

    # 마지막 도시 -> 출발 도시로 돌아오는 비용 추가
    if valid and w[path[-1]][path[0]] != 0:  # 출발지로 돌아오는 길이 있어야 함
        current_cost += w[path[-1]][path[0]]
    else:
        valid = False  # 돌아올 수 없으면 유효한 경로 아님
        
    # 최소 비용 갱신
    if valid:
        min_cost = min(min_cost, current_cost)
        
# 최소 비용 출력
print(min_cost)
