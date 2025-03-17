import sys

input = sys.stdin.readline

prime = [True] * (10001)

for i in range(2, 10001):
    if prime[i]:
        n = i * 2
        while n <= 10000:
            prime[n] = False
            n += i
            
t = int(input())

for _ in range(t):
    num = int(input())
    
    
    for i in range(num // 2, 1, -1):  
        if prime[i] and prime[num - i]:
            print(i, num - i)
            break 