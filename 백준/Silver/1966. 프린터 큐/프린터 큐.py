from collections import deque
import heapq
import sys

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    papers = list(map(int, input().split()))
    
    queue = deque((i,p) for i, p in enumerate(papers))
    max_heap = [-p for p in papers]
    heapq.heapify(max_heap)
    
    count = 0
    
    while queue:
        idx, priority = queue.popleft()
        
        if priority == -max_heap[0]:
            heapq.heappop(max_heap)
            count += 1
            if idx == M:
                print(count)
                break
        else:
            queue.append((idx, priority))