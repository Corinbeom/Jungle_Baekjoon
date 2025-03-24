import sys


N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

count = 0

def lower_bound(arr, target):
    left = 0
    right = len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def lis_length(arr):
    dp = []
    for x in arr:
        pos = lower_bound(dp, x)
        if pos == len(dp):
            dp.append(x)
        else:
            dp[pos] = x
    return len(dp)
        
print(lis_length(arr))