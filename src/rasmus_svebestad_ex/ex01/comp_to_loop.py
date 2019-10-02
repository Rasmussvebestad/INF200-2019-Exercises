# Task B: From comprehension to loop

def squares_by_comp(n):
    return [k ** 2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    squares = []
    for k in range(n):
        if k % 3 == 1:
            squares.append(k ** 2)
    return squares


if __name__ == '__main__':
    if squares_by_comp(10) != squares_by_loop(10):
        print('ERROR!')
