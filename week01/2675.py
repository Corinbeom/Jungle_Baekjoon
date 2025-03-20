tc = int(input())  #  테스트 케이스 횟수 입력
triple = []  #  N번 반복할 문자를 저장할 리스트

for i in range(tc):  #  tc 수 만큼 반복
    n, str = (input().split())  #  n(반복 횟수), str(반복할 문자) 입력
    for j in range(len(str)):   #  str의 길이만큼 반복
        triple += str[j] * int(n)  # triple에 str[j] * n 삽입
    
    print("".join(triple))  #  triple 리스트를 join() 함수로 str로 조합
    n = ""                  #  출력 후 n 초기화
    triple = []             #  출력 후 리스트 초기화
    j = 0                   #  출력 후 j값 초기화
