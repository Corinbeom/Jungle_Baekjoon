def solve(a: list) -> int:
    """리스트의 합을 반환하는 함수"""
    return sum(a)

# 여러 개의 정수를 입력받아 리스트로 변환 (map 사용)
a = list(map(int, input().split()))

# 결과 출력
print(solve(a))