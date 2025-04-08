import sys
input = sys.stdin.readline

n = int(input())  # 도시 수
m = int(input())  # 버스 수

# 인접 행렬 초기화: 모든 거리를 무한대로 시작
INF = int(1e9)
graph = [[INF] * n for _ in range(n)]

# 자기 자신 → 자기 자신은 0
for i in range(n):
    graph[i][i] = 0

# 버스 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)  # 같은 경로 여러 개 있을 수 있음

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) 
            
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
