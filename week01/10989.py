import sys  # 빠른 입력을 위해 sys 모듈 사용

input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

n = int(input())  # 숫자의 개수 입력

# 입력값의 범위가 1부터 10000까지이므로, 이를 담을 배열 생성
arr = [0] * (10000 + 1)  # 0부터 10000까지 총 10001개의 요소를 가진 리스트

# 입력받은 숫자의 개수를 카운트 (계수 정렬 활용)
for _ in range(n):
    arr[int(input())] += 1  # 해당 숫자의 등장 횟수를 증가

# 오름차순으로 출력
for i in range(len(arr)):  # 0부터 10000까지 순회
    if arr[i] != 0:  # 해당 숫자가 등장했다면
        for _ in range(arr[i]):  # 등장 횟수만큼 출력
            print(i)
