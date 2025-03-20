def goUp(top,a,b):  #  달팽이가 최고 높이까지 올라갈떄 필요한 날을 구하는 함수

    todo_up = a - b  # 오늘 올라간 높이
    remain_distane = top - a  # 남은 높이

    today_need = (remain_distane  + todo_up - 1 ) // todo_up  #  오늘 올라가야하는 높이 = (남은 높아 + 오늘 올라간 높이 - 1) // 오늘 올라간 높이

    return today_need + 1  #  오늘 올라가야하는 높이 + 1

numInput = list(map(int, input().split()))  # 입력값 받기

a = numInput[0]  #  달팽이가 낮에 올라간 높이
b = numInput[1]  #  달팽이가 밤에 내려간 높이
top = numInput[2]  #  달팽이가 올라가야 할 높이


print(goUp(top, a, b)) # 함수 호출
