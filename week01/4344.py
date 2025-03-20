c = int(input())  # 테스트케이스 입력

for i in range(c): # c번 반복
    lst = list(map(int, input().split()))  # lst 0번 인덱스에 인원, 1번 인덱스 부터 점수 삽입
    
    sumNum = sum(lst[1:])  # 0번 인덱스 제외하고 합 구하기
    aver = sumNum / (len(lst) - 1)   # 0번 인덱스 제외하고 평균 구하기

    avuLst = [num for num in lst[1:] if num > aver]  # 1번 인덱스부터 점수가 평균보다 높은 점수만 avuLst에 담기

    percent = (len(avuLst) / (len(lst) - 1)) * 100   #  avuLst의 인덱스 수 / (전체 인원 - 1) * 100 (평균 넘는 인원의 퍼센티지 구하기)

    print(f"{percent:.3f}%")  #  결과 소수점 세번째 자리까지 출력
