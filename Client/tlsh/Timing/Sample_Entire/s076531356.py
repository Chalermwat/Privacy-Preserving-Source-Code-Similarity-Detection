#!/usr/bin/env python
# encoding: utf-8

import copy


class Solution:
    def stable_sort(self):
        # write your code here
        array_length = int(input())
        b_array = [str(x) for x in input().split()]
        s_array = copy.deepcopy(b_array)

        bubble_result = self.bubble_sort(b_array=b_array, array_length=array_length)
        selection_result = self.selection_sort(s_array=s_array, array_length=array_length)

        # check whether selection sort is stable
        if bubble_result == selection_result:
            print("Stable")
        else:
            print("Not stable")

    @staticmethod
    def selection_sort(s_array, array_length):
        # selection sort
        selection_count = 0
        for i in range(array_length):
            min_j = i
            for j in range(i, array_length):
                if s_array[j][1] < s_array[min_j][1]:
                    min_j = j
            s_array[i], s_array[min_j] = s_array[min_j], s_array[i]
            if i != min_j:
                selection_count += 1

        result = " ".join(map(str, s_array))
        print(result)
        return result

    @staticmethod
    def bubble_sort(b_array, array_length):
        flag, bubble_count, cursor = 1, 0, 0
        while flag:
            flag = 0
            for j in range(array_length - 1, cursor, -1):
                if b_array[j][1] < b_array[j - 1][1]:
                    b_array[j], b_array[j - 1] = b_array[j - 1], b_array[j]
                    flag = 1
                    bubble_count += 1
        cursor += 1
        result = " ".join(map(str, b_array))
        print(result)
        print("Stable")
        return result


if __name__ == '__main__':
    solution = Solution()
    solution.stable_sort()