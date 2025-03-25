import sys
import bisect

N = int(sys.stdin.readline())

SC = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

CC = list(map(int, sys.stdin.readline().split()))

cards = sorted(SC)

result = []

for target in CC:
    left = bisect.bisect_left(cards, target)
    right = bisect.bisect_right(cards, target)
    count = right - left
    result.append(count)
        
print(*result)