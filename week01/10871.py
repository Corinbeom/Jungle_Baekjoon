import sys  # 빠른 입력을 위해 sys 모듈 사용

# n: 숫자의 개수, x: 기준 값
n, x = map(int, input().split())

# n개의 정수를 입력받아 리스트로 변환 (빠른 입력을 위해 sys.stdin.readline 사용)
numlist = list(map(int, sys.stdin.readline().split()))

reslist = []  # x보다 작은 값들을 저장할 리스트

# 리스트의 모든 요소를 검사
for i in range(len(numlist)):  
    if numlist[i] < x:  # 현재 요소가 x보다 작다면
        reslist.append(numlist[i])  # 결과 리스트에 추가

# 리스트의 요소를 공백으로 구분하여 출력
print(*reslist)
