def get_name():
    return raw_input("What is your name? ").strip()

def get_greeting(name):
    return "Hello, {}, nice to meet you!".format(name)

name = ''

while (len(name) == 0):
    name = get_name()

print get_greeting(name)
