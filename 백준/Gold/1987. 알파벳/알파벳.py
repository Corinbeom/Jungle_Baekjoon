import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C = map(int, input().split())

alphabet = [list(input().strip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_count = 0

visited_state = set()

def dfs(x, y, visited ,depth):
    global max_count
    
    if (x, y, visited) in visited_state:
        return
    visited_state.add((x, y, visited))

    
    max_count = max(max_count, depth)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C:
            idx = ord(alphabet[nx][ny]) - ord('A')
            if not (visited & (1 << idx)):
                dfs(nx, ny, visited | (1 << idx), depth + 1)
                
start = ord(alphabet[0][0]) - ord('A')
dfs(0, 0, 1 << start, 1)
print(max_count)