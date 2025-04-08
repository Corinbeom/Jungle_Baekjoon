import sys
input = sys.stdin.readline

N = int(input())

MOD = 15746
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    print(dp[N])