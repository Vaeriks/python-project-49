from random import randint
import prompt


def welcome_():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    def is_even_games():
        i = 0
        while i < 3:
            number = randint(1, 100)
            print(f'Question: {number}')
            answer_user = prompt.string("Your answer: ")
            if (number % 2 == 0 and answer_user == 'yes') or (
                    number % 2 != 0 and answer_user == 'no'):
                print('Correct!')
                i += 1
            else:
                if number % 2 == 0 and answer_user != 'yes':
                    print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                else:
                    print("'yes' is wrong answer ;(. Correct answer was 'no'.")
    is_even_games()

    print('Congratulations, ' + name + '!')
