first = raw_input("What is the first number? ")
second = raw_input("What is the second number? ")
n1 = int(first)
n2 = int(second)
template = '{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}'
print template.format(first, second, n1 + n2,
                      first, second, n1 - n2,
                      first, second, n1 * n2,
                      first, second, n1 / n2)
