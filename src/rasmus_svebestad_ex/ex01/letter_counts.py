# Task C: Counting letters

import collections as col


def letter_freq(txt):
    a = txt.lower()
    letter_count = {x: a.count(x) for x in set(a)}
    return col.OrderedDict(sorted(letter_count.items(), key=lambda t: t[0]))


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
