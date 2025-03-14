import sys

n, x = map(int, input().split())

numlist = list(map(int,sys.stdin.readline().split()))

reslist = []

for i in range(len(numlist)):
    if numlist[i] < x:
        reslist.append(numlist[i])

print(*reslist)