import prompt
from random import randint


def game():
    first_num = randint(1, 15)
    step = randint(2, 5)
    end_num = (step * 10) + first_num
    posl = range(first_num, end_num, step)
    progress = list(posl)
    i = randint(0, 9)
    answer_1 = progress[i]
    a = str('..')
    result = ''
    for item in progress:
        if item == progress[i]:
            result = result + a + ' '
        else:
            result = result + str(item) + ' '
    print(f'Question: {result}')
    answer_user_1 = prompt.string("Your answer: ")
    return answer_1, answer_user_1
