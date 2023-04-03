import prompt
from random import randint


def game():
    num_1 = randint(1, 15)
    num_2 = randint(1, 15)
    number = f'{num_1} {num_2}'
    print(f'Question: {number}')
    answer_user_1 = prompt.string("Your answer: ")
    num_min = min(num_1, num_2)
    num_max = max(num_1, num_2)
    if num_max % num_min == 0:
        answer_1 = num_min
    else:
        count = 1
        result = []
        end = int(num_min)
        while count <= end:
            if (num_1 % count == 0) and (num_2 % count == 0):
                result.append(count)
                count += 1
            else:
                count += 1
        answer_1 = max(result)
    return answer_1, answer_user_1
