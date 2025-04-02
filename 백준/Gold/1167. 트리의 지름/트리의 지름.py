import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(V):
    data = list(map(int, input().split()))
    for i in range(1, len(data)-1, 2):
        graph[data[0]].append((data[i], data[i+1]))
        
def dfs(node, distance):
    max_distance = distance
    farthest_node = node
    
    for next, weight in graph[node]:
        if visited[next] == False:
            visited[next] = True
            dist, far_node = dfs(next, distance + weight)
            if dist > max_distance:
                max_distance = dist
                farthest_node = far_node
    return max_distance, farthest_node
                
                
visited = [False] * (V+1)
visited[1] = True
_, farthest_from_start = dfs(1, 0)

visited = [False] * (V+1)
visited[farthest_from_start] = True
max_distance, _ = dfs(farthest_from_start, 0)

# 결과 출력
print(max_distance)