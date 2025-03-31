import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

distance = [float('inf')] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        cur_cost, now = heapq.heappop(heap)
        
        if distance[now] < cur_cost:
            continue
        
        for next_node, next_cost in graph[now]:
            total_cost = cur_cost + next_cost
            
            if total_cost < distance[next_node]:
                distance[next_node] = total_cost
                heapq.heappush(heap, (total_cost, next_node))
                



dijkstra(start)
print(distance[end])

