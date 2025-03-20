def is_same(x, y, size):  #  행과 열이 동일한지 확인하는 함수
    first_value = grid[x][y]  #  해당 영역의 첫 번쨰 값을 기준으로 설정

    #  주어진 영역 모두 탐색하여 값이 같은지 확인
    for i in range(x, x + size):  #  행을 순회
        for j in range(y, y+ size):  #  열을 순회
            if grid[i][j] != first_value:  #  하나라도 다른 값이 있다면
                return False  #  False 반환
    return True  #  모든 값이 동일하면 True

def quad_tree(x, y, size):  #  쿼드트리 압축을 수행하는 재귀 함수
    if is_same(x, y, size):  #  현재 영역이 모두 같은 숫자로 이루어져 있다면 (is_same 함수 호출)
        print(str(grid[x][y]), end="")  # 해당 숫자를 출력하고 종료
        return  
    
    print("(", end="")  #  다른 숫자가 섞여있으면 괄호 열기 (분할 시작)
    
    half = size // 2  #  현재 크기를 절반으로 나누어 4등분
    quad_tree(x, y, half)  #  왼쪽 위 부분
    quad_tree(x, y + half, half)  #  오른쪽 위 부분
    quad_tree(x + half, y, half)  #  왼쪽 아래 부분
    quad_tree(x + half, y + half, half)  #  오른쪽 아래 부분
    
    print(")", end="")  #  모든 4개 영역 처리 후 괄호 닫기 (분할 종료)
            

n = int(input())  #  영상의 크기 (NxN) 입력 받기

#  2차원 리스트로 영상 정보 저장 (공백 없이 연속된 숫자로 입력)
grid = [list(map(int, input())) for _ in range(n)] 

quad_tree(0, 0, n)  # 쿼드 트리 실행 (전체 영역을 탐색하여 압축 수행)