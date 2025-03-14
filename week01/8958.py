n = int(input())

for i in range(n):
    oxlist = input()
    score = 0
    sum = 0
    for j in oxlist:
        if j == "O":
            score += 1
        else:
            score = 0
        sum += score

    print(sum)