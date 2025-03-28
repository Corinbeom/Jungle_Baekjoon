import sys
from queue import PriorityQueue
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i
    
for i in range(M):
    start, end, weight = map(int, input().split())
    pq.put((weight, start, end))  #  가중치 기준이기 때문에 가중치를 제일 앞 순서로
    
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        
useEdge = 0
result = 0

while useEdge < N-1:
    weight, start, end = pq.get()
    if find(start) != find(end):
        union(start, end)
        result += weight
        useEdge += 1

print(result)