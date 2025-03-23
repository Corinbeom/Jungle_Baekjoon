import sys

def can_install(h, C, mid):
    count = 1
    last_installed = h[0]
    
    for i in range(1, len(h)):  #  나머지 집들을 순회하면서
        if h[i] - last_installed >= mid:  #  mid 이상 떨어진 집에만 공유기 설치
            count += 1
            last_installed = h[i]
    
    return count >= C  #  설치 개수가 C 이상이면 True 아니면 False
    

N, C = map(int,sys.stdin.readline().split())  #  C : 설치할 공유기 수
h = sorted([int(sys.stdin.readline()) for _ in range(N)])  #  집 좌표 리스트 오름차순 정렬


# 이분 탐색 
start = 1
end = h[-1] - h[0]
result = 0

while start <= end:  #  start가 end를 넘어가면 탐색 종료
    mid = (start + end) // 2  #  공유기 사이의 최소 거리 후보
    if can_install(h, C, mid):  #  설치 가능하면 현재 거리 mid는 답이 될 수 있음
        result = mid      #  result 값에 mid 저장
        start = mid + 1   #  하지만 더 넓은 거리도 가능할 수 있으니 더 넓혀보기
    else:
        end = mid - 1    #  설치 불가능하면 end값에 mid - 1 값 넣기

print(result)