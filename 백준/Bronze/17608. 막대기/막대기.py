import sys

N = int(sys.stdin.readline())  
sticks = [int(sys.stdin.readline()) for _ in range(N)]  

stack = [] 
max_height = 0
count = 0

for i in range(N - 1, -1, -1 ): 
    if sticks[i] > max_height:
        stack.append(sticks[i])
        max_height = sticks[i]
        count += 1 

print(len(stack))