arr = [0] * 10

for i in range(10):
    n = int(input())
    arr[i] = n

tmp_arr = [0] * 10

for j in range(10):
    tmp_arr[j] = arr[j] % 42

tmp_arr = set(tmp_arr)
print(len(tmp_arr))