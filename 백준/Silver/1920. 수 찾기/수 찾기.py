# 자연수 N값 입력
N = int(input())
# N개의 정수 입력
nNum = set(map(int, input().split()))  
# M 입력
M = int(input())
# M개의 수
mNum = list(map(int, input().split()))

# 각 mNum 값이 nNum에 존재하는지 확인
for num in mNum:
    if num in nNum:
        print(1)
    else:
        print(0)