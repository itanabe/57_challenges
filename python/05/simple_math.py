first = None
second = None
n1 = None
n2 = None


def get_two_numbers():
    numbers = [
        ['first', None],
        ['second', None],
    ]

    for number in numbers:
        n = None
        while n is None:
            s = raw_input("What is the " + number[0] + " number? ")
            try:
                n = int(s)
                if n < 0:
                    print("Please enter a non-negative number.")
                    n = None
                    continue
            except:
                continue
        number[1] = n

    return numbers[0][1], numbers[1][1]


def compute(n1, n2):
    add = n1 + n2
    subtract = n1 - n2
    multiply = n1 * n2
    divide = None
    try:
        divide = n1 / n2
    except:
        divide = 'N/A'
    return add, subtract, multiply, divide


def main():
    n1, n2 = get_two_numbers()
    nsum, nsub, nmul, ndiv = compute(n1, n2)
    template = '{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}'
    print template.format(n1, n2, nsum,
                          n1, n2, nsub,
                          n1, n2, nmul,
                          n1, n2, ndiv)

if __name__ == '__main__':
    main()
