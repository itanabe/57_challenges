# -*- coding: utf-8 -*-


class CharCounter(object):
    def __init__(self, input_string):
        self.instr = input_string

    def get_input_string(self):
        return self.instr

    def count_chars(self):
        return len(self.instr)


def main():
    ccount = 0
    while (ccount < 1):
        cc = CharCounter(raw_input("What is the input string? "))
        ccount = cc.count_chars()

        if(ccount > 0):
            plural_suffix = '' if ccount == 1 else 's'

            print '{} has {} character{}.'.format(
            cc.get_input_string(),
            ccount,
            plural_suffix
            )
        else:
            print "The input string must be longer than 0 characters."

if __name__ == '__main__':
    main()
