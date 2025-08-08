done_list = [0] * 28
for i in range(28):
    done_list[i] = int(input())
    
done_list = sorted(done_list)
all_list = [0] * 30

for j in range(30):
    all_list[j] = j+1

all_list_set = set(all_list)
done_list_set = set(done_list)

result = all_list_set.difference(done_list_set)
result = sorted(result)

for i in range(len(result)):
    print(result[i])