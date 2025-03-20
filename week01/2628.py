w, h = map(int, input().split())  # 종이의 가로(w), 세로(h) 길이

n = int(input())  #  자를 횟수

width = [0,w]  # 가로(세로 방향으로 자르는 위치)
height = [0, h]  #  세로(가로 방향으로 자르는 위치)

result = 0  #  가장 큰 종이 조각의 넓이

for _ in range(n):
    a, b = map(int, input().split())  #  방향(a)와 자르는 위치(b) 입력 받기
    if a == 0:     # a가 0이면
        height.append(b)  #  가로 방향으로 자르고 height 리스트에 추가
    elif a == 1:   # a가 1이면 
        width.append(b)   #  세로 방향으로 자르고 width 리스트에 추가

width.sort()     #  가로 정렬
height.sort()    #  세로 정렬

# 모든 조각의 크기 계산하여 최대값 찾기
for i in range(len(width)-1): 
    for j in range(len(height)-1):
        x = width[i+1] - width[j]    #  가로 길이 계산
        y = height[i+1] - height[j]  #  세로 길이 계산
        result = max(result, x*y)    #  최대 넓이 갱신

print(result)