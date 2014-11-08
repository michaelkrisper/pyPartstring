#!/usr/bin/python3
# coding=utf-8
"""
Script for splitting a string into its parts (variable length, all possible combinations in order).
"""

import itertools

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"
__date__ = "2014-11-08"


def split(text):
    parts = {text[i:j] for i in range(0, len(text)) for j in range(i + 1, len(text) + 1)}
    parts = sorted(parts, key=lambda x: (len(x), x))

    solutions = set()
    powerset = itertools.chain.from_iterable(itertools.combinations(parts, r) for r in range(1, len(parts) + 1))
    for sub_parts in powerset:
        sub_solution = set()
        pos = 0
        while pos < len(text):
            for part in sub_parts:
                if text.startswith(part, pos) and ((part in sub_solution) or all(x not in part and part not in x for x in sub_solution)):
                    sub_solution.add(part)
                    pos += len(part)
                    break
            else:
                break
        if pos == len(text):
            solution = tuple(sorted(sub_solution))
            if solution not in solutions:
                yield solution
                solutions.add(solution)

def main():
    print(set(split("abcd")))


if __name__ == "__main__":
    main()