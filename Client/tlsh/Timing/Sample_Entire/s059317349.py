#!/usr/bin/env python
# encoding: utf-8


class Solution:
    @staticmethod
    def stack_polish_calc():
        # write your code here
        # array_length = int(input())
        calc_func = ('+', '-', '*')
        array = [str(x) for x in input().split()]
        # print(array)
        result = []
        for i in range(len(array)):
            if array[i] not in calc_func:
                result.append(str(array[i]))
            else:
                calc = array[i]
                arg_2 = result.pop()
                arg_1 = result.pop()
                result.append(str(eval(''.join((str(arg_1), calc, str(arg_2))))))

        print(*result)


if __name__ == '__main__':
    solution = Solution()
    solution.stack_polish_calc()