def hanoi(N, start, end):  #  하노이 함수 호출(N(입력값), 1(첫번째장판), 3(마지막 장판)
    if N > 1:  #  장판의 갯수가 1개보다 많으면
        hanoi(N-1, start,6-start-end)  #  하노이 함수 호출(N-1(입력값), 1(첫번째장판), 6-1-3= 2()
    print(start, end)
    
    if N > 1:
        hanoi(N-1, 6-start-end, end)

N = int(input())  #  장판 갯수 입력 받기

if N <= 20:  #  N이 20 이하면
    print(2**N-1)  #  이동횟수 출력
    hanoi(N,1,3)   #  하노이 함수 호출(N(입력값), 1(첫번째장판), 3(마지막 장판)

