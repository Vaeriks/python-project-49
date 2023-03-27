import prompt
from random import randint


def game():
    num_1 = randint(1, 50)
    num_2 = randint(1, 50)
    symbol = ['+', '-', '*']
    i = randint(0, 2)
    symbol_game = symbol[i]
    number = f'{num_1} {symbol_game} {num_2}'
    print(f'Question: {number}')
    answer_user_1 = prompt.string("Your answer: ")
    if i == 0:
        answer_1 = num_1 + num_2
    elif i == 1:
        answer_1 = num_1 - num_2
    else:
        answer_1 = num_1 * num_2
    return answer_1, answer_user_1
