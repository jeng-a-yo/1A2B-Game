from random import choices
import os
import sys

def JudgmentSame(x):
    y = list(str(x))
    a = int(y[0])
    b = int(y[1])
    c = int(y[2])
    d = int(y[3])
    if a != b and a != c and a != d and b != c and b != d and c != d:
        return True
    else:
        return False

def CountAB(guessNumber, compareNumber):
    A = 0
    B = 0
    guessNumberList = list(str(guessNumber))
    compareNumberList = list(str(compareNumber))
    for a in range(0, 4):
        if compareNumberList[a] in guessNumberList:
            if compareNumberList[a] == guessNumberList[a]:
                A += 1
            else:
                B += 1
    return [A, B]

def StandardDeviation(*data):
    pass

ANSWER_LIST = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [3, 0], [4, 0]]

allPossibilities = [i for i in range(1023, 9877) if JudgmentSame(i)]
# print(len(allPossibilities))

guessNumber = str(choices(allPossibilities)[0])
guessNumberList = list(guessNumber)

resultDictionary = {}

resultList = allPossibilities.copy()

guessNumber = choices(resultList)[0]

restart = False

for answerOfFirstGuessNumber in allPossibilities:
    resultDictionary.update({answerOfFirstGuessNumber: CountAB(guessNumber, answerOfFirstGuessNumber)})

guessTimes = 0

print("Game Started!")
print("Enter \'interrupt\' to view remaining possibilities.")
print("Enter \'end\' to end the game.")

while True:
    try:
        print("猜測的數字", guessNumber)
        guessTimes += 1

        replyA = input("A有幾個")

        if replyA == "interrupt":
            print(resultList)
            guessTimes -= 1
            continue

        if replyA == "end":
            break

        if int(replyA) == 4:
            print("答案是", guessNumber)
            print("猜了", guessTimes, "次")
            break

        replyB = input("B有幾個")

        if replyB == "interrupt":
            print(resultList)
            guessTimes -= 1
            continue

        if replyB == "end":
            break

        resultList.clear()

        for b in resultDictionary.items():
            if (b[1])[0] == int(replyA) and (b[1])[1] == int(replyB):
                resultList.append(b[0])

        if len(resultList) == 1:
            print("答案是", resultList[0])
            guessTimes += 1
            print("猜了", guessTimes, "次")
            break

        guessNumber = choices(resultList)[0]

        resultDictionary.clear()

        for c in resultList:
            resultDictionary.update({c: CountAB(guessNumber, c)})

    except ValueError:
        print("The entry was incorrect")
        print("The game will restart")
        restart = True
        break

if restart:
    os.system('python 1A2Btest.py')
