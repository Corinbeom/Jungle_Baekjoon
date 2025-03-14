import math

a = int(input())
b = int(input())

a1 = math.trunc(b % 10)
a2 = math.trunc((b / 10) % 10)
a3 = math.trunc((b / 100) % 10)

step1 = a * a1
step2 = a * a2
step3 = a * a3
res = a * b

print("%d" %step1)
print("%d" %step2)
print("%d" %step3)
print("%d" %res)