import sys

N, B = map(int, sys.stdin.readline().split())

A = [(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]

def matrix_pow(A,B):
    if B == 1:
        return [[element % 1000 for element in row] for row in A]
    
    half = matrix_pow(A, B // 2)
    if B % 2 == 0:
        return matrix_mul(half, half)
    else:
        return matrix_mul(matrix_mul(half,half), A)
    

def matrix_mul(A,B):
    N = len(A)
    result = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= 1000
    return result

result = matrix_pow(A, B)
for row in result:
    print(*row)
    
