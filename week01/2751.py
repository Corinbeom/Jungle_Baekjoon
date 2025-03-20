import sys

n = int(input())  #  입력 받기

num_list = []     #  리스트 선언

for _ in range(n):  #  n만큼 반복
    num_list.append(int(sys.stdin.readline()))  #  입력 받은 값을 num_list에 append

for num in sorted(num_list):  #  정렬된 num_list를 반복
    print(num)  #  num의 값 출력