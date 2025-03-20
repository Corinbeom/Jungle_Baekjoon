import math

a = int(input())  # 첫번째 값 입력 받기
b = int(input())  # 두번째 값 입력 받기

a1 = math.trunc(b % 10)  # b의 1의 자리       trunc : 소수점 버리기
a2 = math.trunc((b / 10) % 10) # b의 10의 자리
a3 = math.trunc((b / 100) % 10) # b의 100의 자리

step1 = a * a1  #  a * (b의 1의 자리)
step2 = a * a2  #  a * (b의 10의 자리)
step3 = a * a3  #  a * (b의 100의 자리)
res = a * b  #  a * b 값

print("%d" %step1)  #  a * (b의 1의 자리)
print("%d" %step2)  #  a * (b의 10의 자리)
print("%d" %step3)  #  a * (b의 100의 자리)
print("%d" %res)    #  a * b