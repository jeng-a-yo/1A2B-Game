import random
import os
import sys
# 1A2B computer guess


def juagment_same(x):
    y = list(str(x))
    a = int(y[0])
    b = int(y[1])
    c = int(y[2])
    d = int(y[3])
    if a != b and a != c and a != d and b != c and b != d and c != d:
        return True
    else:
        return False


def countAB(guess_number, compare_number):
    A = 0
    B = 0
    guess_number_list = list(str(guess_number))
    compare_number_list = list(str(compare_number))
    for a in range(0, 4):
        if compare_number_list[a] in guess_number_list:
            if compare_number_list[a] == guess_number_list[a]:
                A += 1
            else:
                B += 1
    return [A, B]


def standard_deviation(*data):
    pass


ANSWER_LIST = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [
    1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [3, 0], [4, 0]]


all_possibilities = []
for range_number in range(1023, 9877):
    if juagment_same(range_number):
        all_possibilities.append(range_number)

guess_number = str(random.sample(all_possibilities, 1)[0])

guess_number_list = list(guess_number)

result_dictionary = {}

result_list = all_possibilities.copy()

guess_number = (random.sample(result_list, 1))[0]

restart = False


for a in all_possibilities:
    result_dictionary.update({a: countAB(guess_number, a)})
times = 0

print("Game Started!")
print("Enter interrupt can interrupt the game")
print("Enter end can end the game")

while True:
    try:
        print("猜測的數字", guess_number)
        times += 1

        reply_A = input("A有幾個")

        if reply_A == "interrupt":
            print(result_list)
            times -= 1
            continue

        if reply_A == "end":
            break

        if int(reply_A) == 4:
            print("答案是", guess_number)
            print("猜了", times, "次")
            break

        reply_B = input("B有幾個")

        if reply_B == "interrupt":
            print(result_list)
            times -= 1
            continue

        if reply_B == "end":
            break

        result_list.clear()

        for b in result_dictionary.items():
            if (b[1])[0] == int(reply_A) and (b[1])[1] == int(reply_B):
                result_list.append(b[0])

        if len(result_list) == 1:
            print("答案是", result_list[0])
            times += 1
            print("猜了", times, "次")

            break

        guess_number = (random.sample(result_list, 1))[0]

        result_dictionary.clear()

        for c in result_list:
            result_dictionary.update({c: countAB(guess_number, c)})

    except ValueError:
        print("The enter was incorrect")
        print("The game will restart")
        restart = True
        break

if restart:
    os.system('python 1A2Btest.py')
