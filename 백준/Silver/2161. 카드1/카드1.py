import sys
from collections import deque

N = int(sys.stdin.readline())

cards = [x for x in range(1,N+1) ]

cards = deque(cards)
remain_list = []

while len(cards) > 1:
    if len(cards) < 1:
        break
    
    remain_list.append(cards.popleft())
    cards.append(cards.popleft())
    
print(*remain_list, cards[0])