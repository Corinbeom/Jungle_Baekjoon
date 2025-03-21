#  나무 자르기 함수 구현
def cut_tree(M, trees):  #  총 가져가야 할 나무의 높이, 나무 리스트 매개변수
    left = 0  #  절단기의 최소 높이 (0부터 시작)
    right = max(trees)  #  절단기의 최대 높이 (가장 높은 나무의 높이)
    result = 0  # 최적의 절단 높이를 저장할 변수
    
    # 이분 탐색 시작
    while left <= right:  #  절단기의 최소 높이가 최대 높이보다 작거나 같아지면 탈출
        remain_cut_sum = 0  #  현재 설정한 높이에서 가져갈 나무 총합

        mid = (left + right ) // 2  # 중간 값 설정(최적의 절단기의 높이를 구할거임) (이분 탐색 핵심)
        
        #  현재 설정한 높이(mid)에서 잘린 나무 길이 합 계산
        for tree in trees: #  trees 리스트를 돌면서
            if tree > mid:  #  tree값이 중간 값보다 크면
                remain_cut_sum += (tree - mid)  #  가져갈 나무 총 합에 (현재 나무의 높이 - 중간값) 추가
        
        if remain_cut_sum >= M:  # 잘린 나무가 총합이 M 이상이라면
            result = mid         # 가능한 절단 높이 중 최댓값 저장
            left = mid + 1       # 더 높은 절단 높이를 탐색
            
        elif remain_cut_sum < M: # 잘린 나무 합이 M 보다 작으면 높이를 낮춰야함
            right = mid - 1      # 더 낮은 절단 높이를 탐색
        
    return result  # 최적의 절단기 높이 반환

N, M = map(int,input().split())

trees = list(map(int, input().split()))

print(cut_tree(M, trees))

