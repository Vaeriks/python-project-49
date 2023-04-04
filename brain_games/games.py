import prompt


def games_(rules, game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rules)
    i = 0
    while i < 3:
        answer, answer_user = game()
        if str(answer) == answer_user:
            print('Correct!')
            i += 1
            if i == 3:
                print(f"Congratulations, {name}!")
        else:
            print(
                f"'{answer_user}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
