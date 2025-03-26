import sys
import heapq

N = int(sys.stdin.readline())

T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

T.sort(key=lambda x: x[0])

heap = []

for c in T:
    start, end = c
    
    if heap and heap[0] <= start:
        heapq.heappop(heap)
        
    heapq.heappush(heap, end)
    
print(len(heap))