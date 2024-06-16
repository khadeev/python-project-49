from random import randint
from brain_games.cli import welcome_user

def brain_even_game():

    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0

    while i < 3:
        number = randint(1, 100)
        print('Question:', number)
        
        answer = input()
        print('Your answer:', answer)

        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break
        else:
            if answer == 'no':
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break

        i += 1

    if i == 3:
        print(f'Congratulations, {name}!')
