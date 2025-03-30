import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

plus, minus, mul, div = map(int, input().split())

min_result = float('inf')
max_result = float('-inf')

def dfs(idx, total, plus, minus, mul, div):
    global min_result
    global max_result
    
    if idx == N:
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        
        return
    
    if plus > 0:
        dfs(idx + 1, total + arr[idx], plus -1, minus, mul, div)
        
    if minus > 0:
        dfs(idx + 1, total - arr[idx], plus, minus - 1, mul, div)
        
    if mul > 0:
        dfs(idx + 1, total * arr[idx], plus, minus, mul - 1, div)
        
    if div > 0:
        if total < 0:
            dfs(idx + 1, -(-total // arr[idx]), plus, minus, mul, div - 1)
        else:
            dfs(idx +1, total // arr[idx], plus, minus, mul, div - 1)
            
dfs(1, arr[0], plus, minus, mul, div)

print(max_result)
print(min_result)
