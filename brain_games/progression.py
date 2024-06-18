from random import randint
from brain_games.cli import welcome_user


def make_progression():
    length = 10
    start = randint(1, 15)
    step = randint(1, 10)

    number = start

    progression = [start, ]

    for i in range(1, length):
        number += step
        progression.append(number)

    position = randint(0, 9)
    result_number = progression[position]

    new_progression = progression
    new_progression[position] = '..'

    return result_number, new_progression

def brain_progression_game():

    name = welcome_user()


    print('What number is missing in the progression?')

    i = 0

    while i < 3:

        result_number, new_progression = make_progression()
        
        print(f'Question:', end=' '); 

        for num in new_progression:
            print(num, end=' ')
        
        answer = input()

        print('Your answer:', answer)

        try:
            if int(answer) == result_number:
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{result_number}'.")
                print(f"Let's try again, {name}!")
                break
        except:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{result_number}'.")
                print(f"Let's try again, {name}!")
                break


        i += 1

    if i == 3:
        print(f'Congratulations, {name}!')
