import sys
input = sys.stdin.readline

N, M = map(int,input().split())

coins = [int(input()) for _ in range(N)]

count = 0

coins.sort(reverse=True)

for coin in coins:
    count += M // coin
    M %= coin
    
print(count)