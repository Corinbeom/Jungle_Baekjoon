import sys
from collections import deque

def dummy(N, apples, moves):
    #  보드 초기화 : (0: 빈칸, 1: 뱀 몸통, 2: 사과)
    board = [[0] * N for _ in range(N)]
    
    #  사과 위치 보드에 표시 (1-based -> 0-based 변환)
    for x, y in apples:
        board[x-1][y-1] = 2 
        
    #  뱀 위치를 deque로 관리 (처음 시작 위치는 (0, 0))
    snake = deque([(0, 0)])
    board[0][0] = 1  #  뱀의 몸이 있는 칸 표시
    
    #  방향: 오른쪽(0), 아래(1), 왼쪽(2), 위(3)
    direction = 0  
    dx = [0, 1, 0, -1]  #  x 방향 변화
    dy = [1, 0, -1, 0]  #  y 방향 변화
    
    time = 0  #  시간 카운터
    move_idx = 0  #  moves 라스트 인덱스 (방향 전환 용)
    
    
    #  루프 시작
    while True:
        # 이동
        time += 1  #  초 증가
        
        #  현재 머리 위치에서 한 칸 이동
        head_x, head_y = snake[-1]
        nx = head_x + dx[direction]
        ny = head_y + dy[direction]
        
        # 충돌 확인
        #  1. 벽에 부딪힘 -> 종료
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            break
        #  2. 자기 몸에 부딪힘 -> 종료
        if board[nx][ny] == 1:
            break
        # 사과 확인
        
        #  3. 이동한 칸에 사과가 있다면 -> 머리만 추가, 꼬리는 그대로
        if (board[nx][ny] == 2):
            snake.append((nx,ny))
            board[nx][ny] = 1  #  뱀 몸 표시
            
        #  4. 사과가 없다면 -> 머리 추가 + 꼬리 제거 (길이 유지)
        elif (board[nx][ny] == 0):
            snake.append((nx,ny))
            board[nx][ny] = 1
            tail = snake.popleft()  #  꼬리 제거
            board[tail[0]][tail[1]] = 0  #  꼬리 자른 자리 빈칸 처리
        
        # 방향 전환
        
        #  5. 현재 시간에 방향 전환이 있다면 수행
        if move_idx < len(moves) and time == moves[move_idx][0]:
            turn = moves[move_idx][1]
            if turn == 'D':  #  오른쪽 회전
                direction = (direction + 1) % 4
            else:  # 'L'  왼쪽 회전
                direction = (direction - 1) % 4
            move_idx += 1  #  다음 방향 전환으로 넘어감
    return time  #  게임 종료 시간 반환


N = int(sys.stdin.readline())

K = int(sys.stdin.readline())

apples = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

L = int(sys.stdin.readline())

moves = [list(sys.stdin.readline().split()) for _ in range(L)]

moves = [(int(x), c) for x, c in moves]

print(dummy(N, apples, moves))
