from random import randint, choice
import operator
from brain_games.cli import welcome_user


def choose_operator():
    my_operator = choice([{'+': operator.add},
                         {'-': operator.sub},
                         {'*': operator.mul}])

    for key, value in my_operator.items():
        operator_str = key
        opetator_func = value

    return operator_str, opetator_func


def brain_calc_game():
    name = welcome_user()

    print('What is the result of the expression?')

    i = 0

    while i < 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)

        operator_str, opetator_func = choose_operator()

        print(f'Question: {number1} {operator_str} {number2}')

        result = opetator_func(number1, number2)

        answer = input()

        print('Your answer:', answer)

        try:
            if int(answer) == result:
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(.", end=' ')
                print(f"Correct answer was '{result}'.")
                print(f"Let's try again, {name}!")
                break
        except Exception:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{result}'.")
            break

        i += 1

    if i == 3:
        print(f'Congratulations, {name}!')
