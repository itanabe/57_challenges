quote = ''
author = ''

while len(quote) == 0:
    quote = raw_input("What is the quote? ").strip()
while len(author) == 0:
    author = raw_input("Who said it? ").strip()

print author + " says, \"" + quote + "\""
