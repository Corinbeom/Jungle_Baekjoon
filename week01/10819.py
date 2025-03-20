from itertools import permutations  # 순열을 생성하기 위해 itertools 모듈의 permutations 사용

n = int(input())  # 배열의 길이 입력

arr = list(map(int, input().split()))  # 공백으로 구분된 정수를 입력받아 리스트로 변환

# 주어진 리스트의 모든 순열 생성
perm = permutations(arr)

max_value = 0  # 최댓값을 저장할 변수 초기화

# 모든 순열을 순회하면서 가장 큰 값 찾기
for p in perm:
    # |p[i] - p[i+1]| 값들의 합 계산
    total = sum(abs(p[i] - p[i + 1]) for i in range(n - 1))
    # 최댓값 갱신
    max_value = max(max_value, total)

# 최댓값 출력
print(max_value)
