import bisect
import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

dp = []

for x in arr:
    pos = bisect.bisect_left(dp, x)
    if pos == len(dp):
        dp.append(x)
    else:
        dp[pos] = x

print(len(dp))