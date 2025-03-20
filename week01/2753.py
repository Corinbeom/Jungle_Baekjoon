year = int(input())  #  연도 입력 받기

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  #  연도가 4의 배수이면서 100의 배수가 아니거나, 400의 배수가 아니면
    print(1)  #  1(윤년일 시) 출력
else: print(0) # 0(아니라면) 출력