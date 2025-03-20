n = int(input())  #  입력받을 개수 입력받기

nums = list(map(int, input().split()))  #  입력 받은 개수만큼 숫자 입력

cnt = 0  #  개수를 세어줄 cnt 변수 선언

for x in nums:   #  x가 nums가 될 때 까지 반복
  for i in range(2, x+1):  #  i(2부터)가 x+1이 될 때 까지 반복
    if x % i == 0:  #  만약 x % i 가 0이고
      if x == i:    #  x 가 i 면
        cnt += 1    #  갯수 증가
      
      break

print(cnt)          #  갯수 프린트