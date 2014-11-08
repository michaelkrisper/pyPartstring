#!/usr/bin/python3
# coding=utf-8
"""

"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import unittest
import part

class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = part.split("abcd")
        self.assertEqual(result, {
                                  {"a", "b", "c", "d"},
                                  {"a", "b", "cd"},
                                  {"a", "bc", "d"},
                                  {"a", "bcd"},

                                  {"ab", "c", "d"},
                                  {"ab", "cd"},

                                  {"abc", "d"},

                                  {"abcd"}
        })

if __name__ == '__main__':
    unittest.main()
