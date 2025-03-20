a = int(input())  # 첫번째값  입력 받기
b = int(input())  # 두번째값  입력 받기
c = int(input())  # 세번째값  입력 받기

result = list(str(a*b*c)) # result를 str로, list로 변환. 값은 a x b

for i in range(10): # 10번 반복
    print(result.count(str(i)))  # result에 i번째 숫자 count해서 숫자 1부터 9까지 갯수 출력