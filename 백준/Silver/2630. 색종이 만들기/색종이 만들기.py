import sys

def count_color(x, y, size):
    global white, blue
    color = arr[x][y]
    same = True
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != color:
                same = False
                break
        if not same:
            break
    if same:
        if color == 0:
            white += 1
        else:
            blue += 1
        return
    else:
        half = size // 2
        count_color(x, y, half)  # 왼쪽 위
        count_color(x, y + half, half)  # 오른쪽 위
        count_color(x + half, y, half)  # 왼쪽 아래
        count_color(x + half, y + half, half)  # 오른쪽 아래
    
    return


N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white = 0
blue = 0

count_color(0, 0, N)

print(white)
print(blue)

