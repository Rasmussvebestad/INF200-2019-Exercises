# Task A


def char_counts(textfilename):

    # Creating the string
    with open(textfilename, 'r', encoding='utf-8') as textfile:
        char_string = textfile.read()

    # Converting the string to
    ord_list = [ord(i) for i in char_string]

    result = [0 for i in range(256)]

    for char in ord_list:
        for i in range(256):
            if char == i:
                result[i] += 1

    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )

