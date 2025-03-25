import sys
import heapq

N = int(sys.stdin.readline())

card_stack = [int(sys.stdin.readline()) for _ in range(N)]

min_heap = []

total_cost = 0

for card in card_stack:
    heapq.heappush(min_heap, card)


while len(min_heap) > 1:
    a = heapq.heappop(min_heap)
    b = heapq.heappop(min_heap)
    cost = a + b
    total_cost += cost
    heapq.heappush(min_heap, cost)

print(total_cost)