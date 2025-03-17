n = int(input())
word = None
wordList = []

for i in range(n):
    word = (input())
    wordList.append(word)

wordList.sort()

for i in range(n):
    print(wordList[i])