n = int(input())

scores = list(map(int, input().split()))
max_score = max(scores)

fix_scores = [0] * n

for i in range(n):
    fix_score = scores[i]/max_score * 100
    fix_scores[i] = fix_score
    # print(fix_scores[i])

result = sum(fix_scores) / n

print(f"{result:.6f}")