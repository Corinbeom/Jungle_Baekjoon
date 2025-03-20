n = int(input())  #  단어의 갯수 입력
word = None  # 단어를 입력받을 word 선언 (안해도 될듯)
wordList = []  #  단어들을 담을 wordList (리스트) 선언

for _ in range(n):  #  n값이 될 때까지 반복
    word = (input())  #  word에 단어 입력
    wordList.append(word)  # wordList에 입력받은 word 삽입

wordList = set(wordList)  #  중복 값 제거
wordList = list(wordList)  #  중복 값 제거 후 다시 리스트로 변환


wordList.sort()  #  오름차순 정렬
wordList.sort(key=len)  #  길이값으로 오름차순 재정렬 (이 코드라인으로 한번에 해결 가능)

for i in range(len(wordList)):  #  wordList의 길이만큼 반복
    print(wordList[i])          #  i번째 wordList값 출력