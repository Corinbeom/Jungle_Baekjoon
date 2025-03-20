n = int(input())  #  입력값 받기

for i in range(9):  #  9번 반복
    result = n * (i+1)  #  n x i+1 결과
    print(f"{n} * {i+1} = {result}")  #  구구단 1부터 9까지 출력