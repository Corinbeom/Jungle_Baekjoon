import sys

def closest_pair(points):
    px = sorted(points, key=lambda x: x[0])  # x 기준 정렬
    py = sorted(points, key=lambda x: x[1])  # y 기준 정렬
    return recursive_closest(px, py)

def recursive_closest(px, py):
    if len(px) <= 3:
        min_dist = float('inf')
        for i in range(len(px)):
            for j in range(i + 1, len(px)):
                dx = px[i][0] - px[j][0]
                dy = px[i][1] - px[j][1]
                dist = dx * dx + dy * dy  # 제곱 거리
                min_dist = min(min_dist, dist)
        return min_dist
    
    mid = (len(px) // 2)
    mid_x = px[mid][0]
    qx, rx = px[:mid] , px[mid:]
    qy = [p for p in py if p[0] <= mid_x]
    ry = [p for p in py if p[0] > mid_x]
    
    d_left = recursive_closest(qx, qy)
    d_right = recursive_closest(rx, ry)
    d = min(d_left, d_right)
    
    
    strip = [p for p in py if abs(p[0] - mid_x) < d]    
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1])**2 >= d:
                break
            dx = strip[i][0] - strip[j][0]
            dy = strip[i][1] - strip[j][1]
            dist = dx * dx + dy * dy
            if dist < d:
                d = dist
    return d

N = int(sys.stdin.readline())

points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

points.sort()

print(closest_pair(points))