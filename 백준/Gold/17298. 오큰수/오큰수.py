import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

stack = []

answer = [-1] * N  # 1. 정답 리스트 기본값 -1로 초기화


for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
    
print(*answer)