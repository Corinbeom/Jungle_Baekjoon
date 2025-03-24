import sys
import heapq


N = int(sys.stdin.readline())

max_heap = []  # 최대힙 (중간값 이하, 파이썬에선 음수로 저장)
min_heap = []  # 최소힙 (중간값 초과)

for _ in range(N):
    nums = int(sys.stdin.readline())
    
    if not max_heap or nums <= -max_heap[0]:
        heapq.heappush(max_heap, -nums)
    else:
        heapq.heappush(min_heap, nums)
        
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    if len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
    print(-max_heap[0])