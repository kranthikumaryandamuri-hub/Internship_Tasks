# Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase

    lines = []

    for i in range(size):
        left = alphabet[size - 1:size - i - 1:-1]
        right = alphabet[size - 1 - i:size]
        letters = left + right
        row = '-'.join(letters).center(4 * size - 3, '-')
        lines.append(row)

    print('\n'.join(lines[:0:-1] + lines))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
