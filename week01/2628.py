w, h = map(int, input().split())

n = int(input())

width = [0,w]
height = [0, h]

result = 0

for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        height.append(b)
    elif a == 1:
        width.append(b)

width.sort()
height.sort()

print(width)
print(height)

for i in range(len(width)-1):
    for j in range(len(height)-1):
        x = width[i+1] - width[j]
        y = height[i+1] - height[j]
        result = max(result, x*y)

print(result)