import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
start = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    dist = [float('INF')] * (N + 1)
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
                heapq.heappush(heap, (new_cost, next_node))
                
    for i in range(1, N + 1):
        if dist[i] == float('inf'):
            print("INF")
        else:
            print(dist[i])
            
            
dijkstra(start)

