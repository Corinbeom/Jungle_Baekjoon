numbers = []  #  9개의 숫자를 받을 리스트 선언
for j in range(9):  # 9번 반복
    i = int(input())  # i에 9개의 숫자를 받아서 int로 변환
    numbers.append(i) # 입력받은 i를 numbers 리스트에 append
    
print(max(numbers))  # numbers 리스트에서 max값 출력
print(numbers.index(max(numbers))+1)  # max값의 index+1 출력 (몇 번째에 있는지)