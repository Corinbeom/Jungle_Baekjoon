def goUp(top,a,b):

    todo_up = a - b  # 4
    remain_distance = top - a  # 1

    today_need = (remain_distance  + todo_up - 1 ) // todo_up

    return today_need + 1

numInput = list(map(int, input().split()))

a = numInput[0] #  달팽이가 낮에 올라간 높이 = numInput[0]
b = numInput[1] #  달팽이가 밤에 내려난 높이 입력 = numInput[1]
top = numInput[2]  #  달팽이가 가야 할 높이 입력 = numInput[2]


print(goUp(top, a, b))
