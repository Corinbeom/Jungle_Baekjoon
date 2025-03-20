x, y, w, h = map(int,input().split())  #  x,y(현재 좌표), w,h(오른쪽 위 꼭짓점)
print(min(x, y, w-x, h-y))  # x, y, w-x, h-y 중 최솟값을 출력