N = int(input())

coins = [1, 5, 10, 50, 100, 500]
coins = sorted(coins, reverse=True)
count = 0

rest_m = 1000 - N

for coin in coins:
    count += rest_m // coin
    rest_m %= coin
print(count)