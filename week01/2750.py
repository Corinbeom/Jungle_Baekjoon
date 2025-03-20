n = int(input())  #  입력 받기
nums = []         #  리스트 선언

for i in range(n):  #  n번 반복
    num = int(input())  #  num 입력 받기
    nums.append(num)    #  nums 리스트에 num 추가

nums.sort()  # nums 리스트 정렬

for j in range(len(nums)):  # nums 길이(최대 인덱스)만큼 반복
    print(nums[j])  #  nums[j] 출력
    

#  수 정렬하기 1