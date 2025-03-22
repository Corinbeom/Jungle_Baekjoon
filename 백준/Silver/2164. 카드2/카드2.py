from collections import deque
import sys

N = int(sys.stdin.readline().strip())

cards = [x for x in range(1, N+1)]

queue = deque()

for i in range(len(cards)):
    queue.append(cards[i])



while True:
    if len(queue) == 1:
        break
    queue.popleft()
    
    queue.append(queue[0])

    queue.popleft()

print(*queue)
    
