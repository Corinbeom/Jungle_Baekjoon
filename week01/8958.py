n = int(input())  # 입력 받을 개수 입력받기

for i in range(n): # n번 반복
    oxlist = input() # OX 리스트 입력 받기
    score = 0  # Score 선언
    sum = 0    # 도합 변수 선언
    for j in oxlist:  # oxlist 반복
        if j == "O":  # j가 O일 때
            score += 1  # score + 1
        else:         # 아니라면
            score = 0 # score 
        sum += score  # sum에 score 합

    print(sum)  