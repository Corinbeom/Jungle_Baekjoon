import sys

def find_bes_pair(sortR):
    left = 0
    right = len(sortR) - 1
    value = 0
    min_diff = float('inf')
    best_pair = (0, 0)
    
    while left < right:
        value = sortR[left] + sortR[right]
        
        if abs(value) < min_diff:
            min_diff = abs(value)
            best_pair = (sortR[left], sortR[right])
        
        if value < 0:
            left += 1
        if value > 0:
            right -= 1
            
        if value == 0:
            return best_pair
    
    return best_pair

N = int(sys.stdin.readline())

R = list(map(int, sys.stdin.readline().split()))

sortR = sorted(R)

print(*find_bes_pair(sortR))

