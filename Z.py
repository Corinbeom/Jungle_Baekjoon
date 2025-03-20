def find_z(n,r,c):
    
    if n == 0:
        return 0
    
    size = 2 ** (n - 1)
    quadrant_size = size * size
    
    if r < size and c < size:
        return find_z(n-1, r, c)
    
    elif r < size and c >= size:
        return quadrant_size + find_z(n - 1, r, c - size)
    
    elif r >= size and c < size:
        return 2 * quadrant_size + find_z(n - 1, r - size, c)
    
    else:
        return 3 * quadrant_size + find_z(n - 1, r - size, c - size)
    
N, r ,c = map(int, input().split())

print(find_z(N,r,c))