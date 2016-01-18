quote = ''
person = ''

while len(quote) == 0:
    quote = raw_input("What is the quote? ").strip()
while len(author) == 0:
    person = raw_input("Who said it? ").strip()

print person + " says, \"" + quote + "\""
