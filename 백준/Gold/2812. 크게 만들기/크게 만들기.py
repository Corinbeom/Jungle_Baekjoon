import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

num = input()  
digits = list(map(int, num))


stack = []

del_cnt = 0

for dig in digits:
    while stack and (del_cnt < K) and stack[-1] < dig:
        stack.pop()
        del_cnt += 1
        
    stack.append(dig)
    
if del_cnt < K:
    stack.pop()
    
print("".join(map(str, stack[:N-K])))
