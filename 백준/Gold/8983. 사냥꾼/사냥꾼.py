import sys

M, N, L = map(int, sys.stdin.readline().split())

attack_p = list(map(int, sys.stdin.readline().split()))

attack_p.sort()

animal_p = []

for _ in range(N):
    i = list(map(int, sys.stdin.readline().split()))
    animal_p.append(i)

def binary_search(attack_p, animal_x, animal_y, L, start, end):
    if start > end:   
        return False
    
    mid = (start + end) // 2
    dist = abs(attack_p[mid] - animal_x) + animal_y

    if dist <= L :   
        return True
    elif attack_p[mid] < animal_x:  
        return binary_search(attack_p, animal_x, animal_y, L, mid + 1, end)
    else :  
        return binary_search(attack_p, animal_x, animal_y, L, start, mid - 1)
        

cnt = 0

for x, y in animal_p:
    if y > L:
        continue
    if binary_search(attack_p, x, y, L, 0, len(attack_p) -1):
        cnt += 1
print(cnt)