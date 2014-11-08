#!/usr/bin/python3
# coding=utf-8
"""
Script for splitting a string into its parts (variable length, all possible combinations in order).
"""

import itertools

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"
__date__ = "2014-11-08"


def min_set(base_set):
    sets = []
    for s in base_set:
        current_set = set()
        for item in s:
            if all(x not in item and item not in x for x in current_set):
                current_set.add(item)
        if current_set not in sets:
            sets.append(current_set)
            yield current_set


def split(text):
    parts = {text[i:j] for i in range(0, len(text)) for j in range(i + 1, len(text) + 1)}
    parts = sorted(parts, key=lambda x: (len(x), x))

    solutions = set()
    powerset = itertools.chain.from_iterable(itertools.combinations(parts, r) for r in range(1, len(parts) + 1))

    for sub_parts in min_set(powerset):
        sub_solution = set()
        pos = 0
        while pos < len(text):
            for part in sub_parts:
                if text.startswith(part, pos):
                    sub_solution.add(part)
                    pos += len(part)
                    break
            else:
                break
        if pos == len(text):
            solution = tuple(sorted(sub_solution))
            if solution not in solutions:
                solutions.add(solution)
                yield solution


def main():
    print(set(split("abcd")))


if __name__ == "__main__":
    main()