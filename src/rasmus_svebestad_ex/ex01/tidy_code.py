from random import randint as a

__author__ = 'Rasmus Svebestad'
__email__ = 'rasmus.svebestad@nmbu.no'


def make_a_guess():
    guess = 0
    while guess < 1:
        guess = int(input('Guess a number from 2 to 12: '))
    return guess


def roll_the_dices():
    return a(1, 6) + a(1, 6)


def check_if_equal(f, g):
    return f == g


if __name__ == '__main__':

    h = False
    number_of_points = 3
    correct_answer = roll_the_dices()
    while not h and number_of_points > 0:
        your_guess = make_a_guess()
        h = check_if_equal(correct_answer, your_guess)
        if not h:
            print('Wrong, try again!')
            number_of_points -= 1

    if number_of_points > 0:
        print('You won {} points.'.format(number_of_points))
    else:
        print('You lost. Correct answer: {}.'.format(correct_answer))

