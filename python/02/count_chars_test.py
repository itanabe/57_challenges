# -*- coding: utf-8 -*-

import unittest
from count_chars import CharCounter


class TestCharCounter(unittest.TestCase):
    def test_happy_path(self):
        cc = CharCounter('Ichiko Tanabe')
        self.assertEqual(13, cc.count_chars())

    def test_0_chars(self):
        cc = CharCounter('')
        self.assertEqual(0, cc.count_chars())

    def test_1_space(self):
        cc = CharCounter(' ')
        self.assertEqual(1, cc.count_chars())

    def test_1_char(self):
        cc = CharCounter('')
        self.assertEqual(0, cc.count_chars())

    def test_non_ascii_western_char(self):
        cc = CharCounter(u"á")
        self.assertEqual(1, cc.count_chars())

    def test_double_byte_char(self):
        cc = CharCounter(u"市")
        self.assertEqual(1, cc.count_chars())

if __name__ == '__main__':
    unittest.main()