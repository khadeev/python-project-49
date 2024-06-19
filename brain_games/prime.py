from random import randint
from brain_games.cli import welcome_user


def brain_prime_game():
    name = welcome_user()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    i = 0

    while i < 3:
        number = randint(2, 97)

        print('Question: ', number)

        divisors = 0

        for j in range(1, number + 1):
            if number % j == 0:
                divisors += 1

        result = 'yes' if divisors == 2 else 'no'

        answer = input()

        print('Your answer:', answer)

        if answer == result:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break

        i += 1

    if i == 3:
        print(f'Congratulations, {name}!')
