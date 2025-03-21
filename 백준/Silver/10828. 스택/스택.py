from collections import deque
import sys

N = int(sys.stdin.readline().strip())  

stack = []

for _ in range(N):
    command = sys.stdin.readline().strip().split()  # 입력을 받고 공백 기준으로 나눔
    

    if command[0] == "push":
        num = int(command[1])  # push 뒤의 숫자
        stack.append(num)

    elif command[0] == "pop":
        print(stack.pop() if stack else -1)

    elif command[0] == "size":
        print(len(stack))  # 현재 스택 크기 출력

    elif command[0] == "empty":
        print(1 if not stack else 0)

    elif command[0] == "top":
        print(stack[-1] if stack else -1)  # 스택의 최상단 원소 출력
