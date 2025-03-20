from itertools import* # itertools 사용

N, S = map(int, input().split())  #  정수의 개수 N, 정수 S

arr = map(int, input().split())   #  N 개의 정수 입력

cnt = 0  #  가능한 경우의 수 카운트

res_arr = list(arr)  #  res_arr로 입력 값들 리스트 선언

for r in range(1, len(res_arr)+1):  # 부분집합의 크기를 1부터 res_arr의 전체 길이까지 증가시키며 반복  
    for combo in combinations(res_arr, r):  #  중복 없이 r개의 원소를 선택하는 모든 경우 반환
        s = sum(combo)  #  선택된 조합의 합을 계산
        if s == S:  #  조합의 합이 S와 같다면
            cnt += 1  #  카운트 1 증가
            
print(cnt)  # 카운트 출력

