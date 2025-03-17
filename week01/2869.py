def goUp(top,a,b):

    todo_up = a - b  # 4
    remain_distane = top - a  # 1

    today_need = (remain_distane  + todo_up - 1 ) // todo_up

    return today_need + 1

numInput = list(map(int, input().split()))

a = numInput[0]
b = numInput[1]
top = numInput[2]


print(goUp(top, a, b))
