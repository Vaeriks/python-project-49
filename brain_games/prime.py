import prompt
from random import randint


def game():
    number = randint(1, 50)
    print(f'Question: {number}')
    answer_user_1 = prompt.string("Your answer: ")
    count = 1
    result = []
    end = int(number / 2)
    while count < end:
        if number % count == 0:
            result.append(count)
            count += 1
        else:
            count += 1
    if result == [1]:
        answer_1 = 'yes'
    else:
        answer_1 = 'no'
    return answer_1, answer_user_1
