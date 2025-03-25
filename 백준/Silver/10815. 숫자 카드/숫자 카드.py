import sys
import bisect

N = int(sys.stdin.readline())

SC = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

CC = list(map(int, sys.stdin.readline().split()))

cards = sorted(SC)

for target in CC:
    idx = bisect.bisect_left(cards, target)
    if idx < len(cards) and cards[idx] == target:
        print(1, end=" ")
    else:
        print(0, end=" ")