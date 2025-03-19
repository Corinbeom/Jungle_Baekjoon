def is_same( x, y, size):
    first_value = grid[x][y]
    
    for i in range(x, x + size):
        for j in range(y, y+ size):
            if grid[i][j] != first_value:
                return False
    return True

def quad_tree(x, y, size):
    if is_same(x, y, size):
        print(str(grid[x][y]), end="")
        return
    
    print("(", end="")
    
    half = size // 2
    quad_tree(x, y, half)
    quad_tree(x, y + half, half)
    quad_tree(x + half, y, half)
    quad_tree(x + half, y + half, half)
    
    print(")", end="")
            

n = int(input())

grid = [list(map(int, input())) for _ in range(n)]

quad_tree(0, 0, n)