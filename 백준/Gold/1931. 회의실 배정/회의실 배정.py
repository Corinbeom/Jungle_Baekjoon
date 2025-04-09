import sys
input = sys.stdin.readline

N = int(input())

times = []

for _ in range(N):
    s, e = map(int, input().split())
    
    times.append((s,e))

times.sort(key=lambda x: (x[1], x[0]))
end = 0
count = 0

for s, e in times:
    if s >= end:
        count += 1
        end = e
print(count)