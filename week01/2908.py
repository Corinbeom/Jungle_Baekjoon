numInput = list(map(int, input().split()))  #  숫자 두개 입력받기

num1 = numInput[0]  #  num1 = numInput[0]
num2 = numInput[1]  #  num2 = numInput[1]

reversedNum1 = list(reversed(str(num1)))  #  num1을 string으로 변환 후 reverse 후 리스트에 저장
reversedNum2 = list(reversed(str(num2)))  #  num2를 string으로 변환 후 reverse 후 리스트에 저장

reversedNum1 = int(''.join(reversedNum1)) #  reverseNum1을 int로 변환
reversedNum2 = int(''.join(reversedNum2)) #  reverseNum2을 int로 변환

if reversedNum1 > reversedNum2:  #  둘의 값 비교 후 reversedNum1이 더 클 경우
    print(reversedNum1)    #  reversedNum1 출력

elif reversedNum1 < reversedNum2:  #  reversedNum1이 reversedNum2보다 작을 경우
    print(reversedNum2)    #  reversedNum2 출력