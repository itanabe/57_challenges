def create_story(n, v, adj, adv):
    return "Do you {} your {} {} {}? That's hilarious!".format(v, adj, n, adv)

noun = raw_input("Enter a noun: ")
verb = raw_input("Enter a verb: ")
adj = raw_input("Enter an adjective: ")
adv = raw_input("Enter an adverb: ")
print create_story(noun, verb, adj, adv)
