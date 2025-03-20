from itertools import combinations

N, M = map(int, input().split())

cards = list(map(int, input().split()))

triple = combinations(cards, 3)

close_cards = list(triple)

able_list = []

for i in range(1, len(close_cards)):
    if int(sum(close_cards[i])) <= M:
        able_list.append(sum(close_cards[i]))

print(max(able_list))