import sys

N = int(sys.stdin.readline())

budget = list(map(int, sys.stdin.readline().split()))

limit = int(sys.stdin.readline())


start = 0
end = max(budget)
answer = 0
    
while start <= end:
    mid = (start + end) // 2
    total_allocated = sum(min(b, mid) for b in budget)
    
    if total_allocated <= limit:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(answer)