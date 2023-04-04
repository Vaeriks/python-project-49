import prompt
from random import randint


def game():
    number = randint(1, 100)
    print(f'Question: {number}')
    answer_user_1 = prompt.string("Your answer: ")
    if number % 2 == 0:
        answer_1 = 'yes'
    else:
        answer_1 = 'no'
    return answer_1, answer_user_1
