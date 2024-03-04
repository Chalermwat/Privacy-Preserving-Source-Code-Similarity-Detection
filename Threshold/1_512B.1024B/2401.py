#!usr/bin/env python3

import sys
import operator
from math import floor


def string_to_list_spliter():
    lst = [int(i) if isinstance(i, int) == True else i for i in sys.stdin.readline().split()]
    return lst


def main():
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    while True:
        lst = string_to_list_spliter()
        if lst[1] == '?':
            break
        elif lst[1] == '+':
            print(ops[lst[1]](int(lst[0]), int(lst[2])))
        elif lst[1] == '-':
            print(ops[lst[1]](int(lst[0]), int(lst[2])))
        elif lst[1] == '*':
            print(ops[lst[1]](int(lst[0]), int(lst[2])))
        elif lst[1] == '/':
            print(floor(ops[lst[1]](int(lst[0]), int(lst[2]))))


if __name__ == '__main__':
    main()