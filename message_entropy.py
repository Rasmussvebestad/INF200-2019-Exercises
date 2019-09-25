# Task B


def letter_freq(txt):
    a = txt.lower()
    letter_count = {x: a.count(x) for x in set(a)}
    return col.OrderedDict(sorted(letter_count.items(), key=lambda t: t[0]))


def entropy(message):
    n_i = letter_freq(message)
    p_i = []
    sum_i = sum(n_i)
    for i in n_i:
        p_i.append(i/sum_i)
    S = 0
    for i in range(len(p_i))
        S += -(p_i(i)*log_2(p_i(i)))
    return S




if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))

