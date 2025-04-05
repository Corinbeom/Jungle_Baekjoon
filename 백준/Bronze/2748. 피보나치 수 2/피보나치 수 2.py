import sys
input = sys.stdin.readline

N = int(input())

dp = [-1] * 100

def fib(N):
    if N <= 1:
        return N
    if dp[N] != -1:
        return dp[N]
    dp[N] = fib(N-1) + fib(N-2)
    return dp[N]

print(fib(N))