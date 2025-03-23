import sys

def power(A, B):
    if B == 1:
        return A % C
    
    temp = power(A, B // 2)
    
    if B % 2 == 0:
        return (temp * temp) % C
    elif B % 2 != 0:
        return (temp * temp * A) % C

A, B, C = map(int,sys.stdin.readline().split())

print(power(A, B))
