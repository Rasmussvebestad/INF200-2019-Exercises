# Task B


import collections as col
import math as m
import numpy as np


def letter_freq(txt):
    a = txt.lower()
    letter_count = {x: a.count(x) for x in set(a)}
    return col.OrderedDict(sorted(letter_count.items(), key=lambda t: t[0]))


def entropy(message):
    n_i = list(letter_freq(message).values())

    p_i = [0 for i in range(len(n_i))]
    sum_i = 0

    for i in n_i:
        sum_i += i

    for i in range(len(n_i)):
        p_i[i] = n_i[i]/sum_i

    S = 0
    for i in p_i:
        S += -(i*m.log2(i))
    return S




if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))

