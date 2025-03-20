# 사용자로부터 입력받아 n개의 테스트 케이스 실행
n = int(input())  # 테스트 케이스 개수 입력

# n번 반복하여 두 수를 입력받고 합을 출력
for i in range(n):  
    a, b = map(int, input().split())  # 두 정수를 입력받음
    res = a + b  # 두 정수의 합 계산
    print(res)  # 결과 출력
