def plus(a, b):
    return a + b  # 덧셈 함수

def minus(a, b):
    return a - b  # 뺄셈 함수

def multiply(a, b):
    return a * b  # 곱셈 함수

def divide(a, b):
    return a / b  # 나눗셈 함수 (실수형 반환)

def remain(a, b):
    return a % b  # 나머지 연산 함수

# 사용자 입력 (공백으로 구분된 두 정수 입력받기)
a, b = map(int, input().split())

# 연산 수행 및 결과 출력
print(plus(a, b))      # 덧셈 결과 출력
print(minus(a, b))     # 뺄셈 결과 출력
print(multiply(a, b))  # 곱셈 결과 출력

# 나눗셈 결과는 소수점까지 출력하도록 변경
print("{:.2f}".format(divide(a, b)))  # 실수 출력 형식 지정

print(remain(a, b))    # 나머지 연산 결과 출력