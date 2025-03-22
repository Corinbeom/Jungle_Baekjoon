from collections import deque
import sys

N = int(sys.stdin.readline().strip())
towers = list(map(int, sys.stdin.readline().split()))

stack = deque()

result = []

for i in range(N):
    while stack and towers[i] >= stack[-1][1]:
        stack.pop()
    
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0] + 1)
        
    stack.append((i,towers[i]))
    
print(*result) 