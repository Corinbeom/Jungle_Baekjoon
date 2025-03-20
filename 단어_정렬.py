n = int(input())
word = None
wordList = []

for i in range(n):
    word = (input())
    wordList.append(word)


wordList = set(wordList)
wordList = list(wordList)


wordList.sort()
wordList.sort(key=len)

for i in range(len(wordList)):
    print(wordList[i])