import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        cur_dist, now = heapq.heappop(heap)
        
        if cur_dist > dist[now]:
            continue
        
        for next_node, cost in graph[now]:
            new_cost = cur_dist + cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(heap,(new_cost, next_node))
                
    return dist

v1, v2 = map(int, input().split())

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

route1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
route2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

result = min(route1, route2)

if result == float('inf'):
    print(-1)
else:
    print(result)