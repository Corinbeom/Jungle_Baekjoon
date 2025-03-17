numInput = list(map(int, input().split()))

num1 = numInput[0]
num2 = numInput[1]

reversedNum1 = list(reversed(str(num1)))
reversedNum2 = list(reversed(str(num2)))

reversedNum1 = int(''.join(reversedNum1))
reversedNum2 = int(''.join(reversedNum2))

if reversedNum1 > reversedNum2:
    print(reversedNum1)

elif reversedNum1 < reversedNum2:
    print(reversedNum2)