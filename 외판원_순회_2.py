from itertools import permutations

n = int(input())  #  도시의 수 입력받기

# 비용 행렬 입력 (N x N)
w = [list(map(int, input().split())) for _ in range(n)]

min_cost = float('inf')  

cities = range(n)

# 모든 방문 순서(순열) 생성
all_paths = permutations(cities)

for path in all_paths:
    current_cost = 0
    valid = True
    
    # 경로를 따라가면서 비용 계산
    for i in range(n-1):
        if w[path[i]][path[i+1]] == 0:  #  길이 없으면 중단
            valid = False
            break
        current_cost += w[path[i]][path[i+1]]
        
        if current_cost >= min_cost:  # 현재 비용이 이미 최소 비용보다 크다면 더 볼 필요 없이 중단
            valid = False
            break
        
    #  마지막 도시 -> 출발 도시로 돌아오는 비용 추가
    if valid and w[path[-1]][path[0]] != 0:
        current_cost += w[path[-1]][path[0]]
    else:
        valid = False
        
    #  최소 비용 갱신
    if valid:
        min_cost = min(min_cost, current_cost)
        
#  최소 비용 출력
print(min_cost)
    
