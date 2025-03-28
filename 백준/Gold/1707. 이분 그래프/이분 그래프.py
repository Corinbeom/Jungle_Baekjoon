import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

K = int(input()) 

for _ in range(K):
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    colors = [-1] * (V + 1)
    is_bipartite = True

    def dfs(node, color):
        colors[node] = color
    
        for neighbor in graph[node]:
            if colors[neighbor] == -1:
                if not dfs(neighbor, 1 - color):
                    return False
            elif colors[neighbor] == color:
                return False
        return True


    for i in range(1, V + 1):
        if colors[i] == -1:  # 아직 방문 안 한 노드
            if not dfs(i, 0):  # 색 0부터 시작
                is_bipartite = False
                break
    


    if is_bipartite:
        print("YES")
    else:
        print("NO")

