def get_name():
    return raw_input("What is your name? ").strip()

def get_greeting(name):
    return "Hello, {}, nice to meet you!".format(name)

name = get_name()
greeting = get_greeting(name)
print greeting