n = int(input())  # 입력 받기

# 처음 입력한 값을 저장
initial = n

# 한 자릿수일 경우, 2자리로 맞추기 위해 앞에 0을 붙여준다.
if n < 10:
    n = int(f"0{n}")

# 사이클을 반복할 변수
count = 0

# 초기값과 같을 때까지 반복
while True:
    first_digit = n // 10  # 첫 번째 자릿수
    second_digit = n % 10  # 두 번째 자릿수
    new_num = (first_digit + second_digit) % 10 + second_digit * 10  # 새로 만든 수

    count += 1  # 사이클 횟수 증가
    
    # 새로 만든 수가 초기값과 같으면 종료
    if new_num == initial:
        break

    # 현재 n을 새로운 값으로 업데이트
    n = new_num

print(count)  # 반복 횟수 출력
