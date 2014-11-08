#!/usr/bin/python3
# coding=utf-8
"""

"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import unittest

import part


class MyTestCase(unittest.TestCase):

    def test_empty(self):
        result = part.split("")
        self.assertEqual(set(result), set())

    def test_onechar(self):
        result = part.split("a")
        self.assertEqual(set(result), {("a",)})

    def test_twochars(self):
        result = part.split("ab")
        self.assertEqual(set(result), {("a", "b"), ("ab",)})

    def test_threechars(self):
        result = part.split("abc")
        self.assertEqual(set(result), {("a", "b", "c"), ("a", "bc"), ("ab", "c"), ("abc",)})

    def test_repetition(self):
        result = part.split("abab")
        self.assertEqual(set(result), {("a", "b"), ("ab",), ("abab",)})

    def test_diff_parts(self):
        result = part.split("abzabx")
        self.assertEqual(set(result),
                         {("a", "b", "x", "z"), ("a", "bx", "bz"), ("ab", "x", "z"), ("ab", "bx", "za"), ("abx", "abz"),
                          ("abza", "bx"), ("abzab", "x"), ("abzabx",)})


if __name__ == '__main__':
    unittest.main()
