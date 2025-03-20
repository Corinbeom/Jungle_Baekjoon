def han(n):  
    count = 0  #  한수의 개수를 저장할 변수 선언
    for i in range(1,n+1):  #  1부터 n+1까지 반복
        a = str(i)  #  a에 문자열로 i 받음
        if len(a) <= 2:  #  a의 길이가 2보다 작거나 같으면 (2자리수거나 한자릿수면, 1-9 or 10-99)
            count = count + 1  #  카운트 증가
        elif len(a)== 3:  #  a의 길이가 3과 같으면 (3자릿수 이면, 100-999)
            if int(a[0]) - int(a[1]) == int(a[1]) - int(a[2]):             # int로 형변환을 하며 
                count = count + 1   # 카운트 1 증가                           # [0번 인덱스 - 1번인덱스] - [0번 인덱스 - 1번인덱스] 비교
        elif len(a) == 4: #  a의 길이가 3과 같으면 (4자릿수 이면, 1000-9999)
            if int(a[0]) - int(a[1]) == int(a[1]) - int(a[2]) == int(a[2]) - int(a[3]):
                count = count + 1
                
    print(count)

n = int(input())  #  입력값 받기

han(n)  #  한수 구하는 함수 한구함 ㅋㅋ