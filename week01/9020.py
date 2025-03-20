import sys # sys 모듈을 가져옴 (빠른 입력을 사용하기 위해 필요함)

input = sys.stdin.readline # 빠른 입력을 위해 sys.stdin.readline을 사용

# 에라토스테네스의 체를 이용한 소수 판별 리스트 초기화
prime = [True] * (10001) # 0부터 10000까지의 숫자가 소수인지 여부를 저장하는 리스트

# 에라토스테네스의 체 알고리즘을 사용하여 소수 리스트 생성
for i in range(2, 10001): # 2부터 10000까지 반복
    if prime[i]:  # 현재 숫자가 소수라면
        n = i * 2  # 해당 숫자의 배수들을 제거하기 시작
        while n <= 10000:  # 10000 이하의 모든 배수를 False로 설정
            prime[n] = False  # 소수가 아님을 표시
            n += i  #  다음 배수로 이동
            
t = int(input())  #  테스트 케이스 개수 입력

for _ in range(t):  # t번 반복
    num = int(input())  #  입력값 (짝수) 받기
    
    # 두 소수의 차이가 가장 작은 골드바흐 파티션을 찾기 위해 반으로 나눈 값부터 탐색
    for i in range(num // 2, 1, -1):    # 중간값에서 시작해서 점점 작은 값으로 이동
        if prime[i] and prime[num - i]: # 두 수가 모두 소수라면
            print(i, num - i)  # 출력
            break  # 가장 차이가 작은 경우를 찾았으므로 종료