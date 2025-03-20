import sys
sys.setrecursionlimit(10**4)  #  재귀함수 제한 10^4

input = sys.stdin.readline  

size = int(input())  #  체스판 사이즈 입력

col = [0 for _ in range(size)]  #  행을 size 만큼 0 리스트 선언
row = [0 for _ in range(size)]  #  열을 size 만큼 0 리스트 선언
diagonal_p = [0 for _ in range(2 * size)]  #  우상향 대각선 공격 가능성 체크 size * 2 만큼 리스트 선언
diagonal_m = [0 for _ in range(2 * size)]  #  우하향 대각선 공격 가능성 체크 size * 2 만큼 리스트 선언

def find_perfect(state):  #  N-Queen 문제를 해결하기 위한 재귀함수
    res = 0
    if state == size:  # 만약 모든 행에 퀸을 배치했다면 (state == size)
        return 1       # 1 리턴
    else:
        for i in range(size):  # 현재 행에 각 열에 대해 퀸을 배치할 수 있는지 확인
            if col[i]:         # 이미 해당 열에 퀸이 배치되어 있다면
                continue       # 다음 열로 넘어감
            check_diagonal_p = state + (size - i)   # 현재 위치의 대각선 인덱스 계산
            check_diagonal_m = i + state 
            if diagonal_p[check_diagonal_p]:        #  대각선 공격 가능성 체크
                continue                            #  있다면 다음 열로 넘어감
            if diagonal_m[check_diagonal_m]:        #  위와 동일
                continue
            col[i] = 1
            diagonal_p[check_diagonal_p] = 1        # 퀸 배치가 가능한 위치라면 해당 위치에 퀸 배치 표시 (1)
            diagonal_m[check_diagonal_m] = 1        # 퀸 배치가 가능한 위치라면 해당 위치에 퀸 배치 표시 (1)
            res += find_perfect(state+1)            # 재귀적으로 함수 호출
            col[i] = 0                              # 백트래킹으로 이전 상태로 되돌림
            diagonal_p[check_diagonal_p] = 0
            diagonal_m[check_diagonal_m] = 0
            
        return res                                  # 모든 가능한 경우의 수 반환
        
print(find_perfect(0))