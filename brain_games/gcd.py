from random import randint
from brain_games.cli import welcome_user


def find_gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num2

def brain_gcd_game():

    name = welcome_user()

    print('Find the greatest common divisor of given numbers.')

    i = 0

    while i < 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        
        print(f'Question: {number1} {number2}')

        result = find_gcd(number1, number2)
        
        answer = input()

        print('Your answer:', answer)

        try:
            if int(answer) == result:
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
                print(f"Let's try again, {name}!")
                break
        except:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
                print(f"Let's try again, {name}!")
                break


        i += 1

    if i == 3:
        print(f'Congratulations, {name}!')
