first = None
second = None
n1 = None
n2 = None

while (n1 is None):
    first = raw_input("What is the first number? ")
    try:
        n1 = int(first)
        if n1 < 0:
            n1 = None
            print ("Please enter non-negative number")
            continue
    except:
        continue

while (n2 is None):
    second = raw_input("What is the second number? ")
    try:
        n2 = int(second)
        if n1 < 0:
            n2 = None
            print ("Please enter non-negative number")
            continue
    except:
        continue

template = '{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}'
print template.format(first, second, n1 + n2,
                      first, second, n1 - n2,
                      first, second, n1 * n2,
                      first, second, n1 / n2)
