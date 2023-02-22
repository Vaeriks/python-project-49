import prompt

def welcome_user():
    name = prompt.string(f'May I have your name? ')
    print('Hello, ' + name + '!')