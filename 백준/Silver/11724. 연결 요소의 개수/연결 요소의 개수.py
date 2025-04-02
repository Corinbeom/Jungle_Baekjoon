import sys
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i
    
def union(a,b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a
        
def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

for _ in range(M):
    a, b = map(int, input().split())
    union(a,b)
    
roots = set()
for i in range(1, N+1):
    roots.add(find(i))
print(len(roots))