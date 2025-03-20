def find_z(n,r,c):  #  n, r, c 매개변수 
    
    if n == 0:  #  n이 0이라면
        return 0  # 0 리턴
    
    size = 2 ** (n - 1)  #  사이즈(2차원 배열 크기)는 2^n-1
    quadrant_size = size * size  #  사분면 사이즈는 size X size
    
    if r < size and c < size:  #  r(행)이 사이즈보다 작고 c(열)이 사이즈보다 작으면
        return find_z(n-1, r, c)  #  n에 1을 뺀 값으로 find_z함수 호출
    
    elif r < size and c >= size:  #  r(행)이 사이즈보다 작고 c(열)이 사이즈보다 크거나 같으면
        return quadrant_size + find_z(n - 1, r, c - size)  #  n에 1을 뺀 값과 c에 size를 뺸 값으로 find_z함수 호출
    
    elif r >= size and c < size:  #  r(행)이 사이즈보다 크거나 같고 c(열)이 사이즈보다 작으면
        return 2 * quadrant_size + find_z(n - 1, r - size, c)  #  n에 1을 뺀 값과 r에 size를 뺸 값으로 find_z함수 호출
    
    else:
        return 3 * quadrant_size + find_z(n - 1, r - size, c - size) 
                                #  n에 1을 뺀 값과 r에 size를 뺀 값과 c에 size를 뺸 값으로 find_z함수 호출
                                
N, r ,c = map(int, input().split())  #  배열 크기 N, 행 r, 열 c 입력 받기

print(find_z(N,r,c))  #  함수 출력