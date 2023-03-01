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
                if i == 3:
                    print('Congratulations, ' + name + '!')
            else:
                if number % 2 == 0 and answer_user != 'yes':
                    print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                    print("Let's try again, " + name + '!')
                    break
                else:
                    print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                    print("Let's try again, " + name + '!')
                    break

    is_even_games()
