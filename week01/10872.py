def factorial(n):
    """
    팩토리얼을 계산하는 함수 (재귀 방식)
    
    n! = n * (n-1)!  
    예) 5! = 5 × 4 × 3 × 2 × 1
    
    - n이 0 또는 1이면 팩토리얼 값은 1 (기저 사례)
    - 그렇지 않으면 n * (n-1)! 재귀 호출
    """
    if n == 0 or n == 1:  # 0! = 1, 1! = 1
        return 1
    else:
        return n * factorial(n - 1)  # 재귀 호출

# 사용자 입력 받기
num = int(input("팩토리얼을 계산할 숫자를 입력하세요: "))

# 팩토리얼 계산
result = factorial(num)

# 결과 출력
print(result)
