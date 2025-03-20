#  난쟁이들의 키를 넣을 배열 선언
arr = [] 


for _ in range(9): # 난쟁이 수만큼 반복
    dwarfs = int(input())  #  난쟁이의 키 입력
    arr.append(dwarfs)  # 아까 선언한 배열에 난쟁이들 키를 삽입
arr.sort()    #  난쟁이의 키들을 내림차순으로 정렬

sum_ = sum(arr)  #  난쟁이들의 키를 모두 합한다
fake = []  #  리얼 난쟁이들의 키의 합은 100이기에 조건에 부합하지않는 가짜 난쟁이를 넣을 배열 선언

for i in range(9):  #  난쟁이 수만큼 반복
    for j in range(i+1,9):  #  가짜 난쟁이를 판별하기 위해 j는 i보다 1이 큰 상태로 반복문 시작
        if(len(fake) == 2):  #  만약 가짜 난쟁이의 인덱스 값(길이)이 2라면
            continue         #  계속
        if sum_ - arr[i] - arr[j] == 100:  #  모든 난쟁이(가짜포함)의 키의 합 - 난쟁이[i] - 난쟁이[j] 의 값이 100이라면
            fake.append(arr[i])  #  난쟁이[i]를 가짜 난쟁이 배열에 삽입         #  값이 100이 아니라면 j 증가 후 반복문 계속 
            fake.append(arr[j])  #  난쟁이[j]를 가짜 난쟁이 배열에 삽입
            
for i in arr:  #  난쟁이 배열을 i로 반복 
    if i in fake:  #  만약 i번째 난쟁이가 가짜 난쟁이 배열 안에 있다면
        continue   #  출력하지 않고 반복문 계속
    print(i)       #  i번째 난쟁이가 가짜 난쟁이 배열 안에 없다면 출력