from collections import deque
import sys

N = int(sys.stdin.readline().strip())  

stack = deque()

for _ in range(N):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push":
        stack.appendleft(command[1])
        
    if command[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    
    if command[0] == "size":
        print(len(stack))
        
    if command[0] == "empty":
        if not stack:
            print(1)
        else: print(0)
        
    if command[0] == "front":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
        
    if command[0] == "back":
        if not stack:
            print(-1)
        else:
            print(stack[0])