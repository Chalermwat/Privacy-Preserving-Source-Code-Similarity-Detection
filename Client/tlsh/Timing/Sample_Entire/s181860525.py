# -*- coding: utf-8 -*-


def bubble_sort(c):
    c = list(c)
    for i in range(len(c)):
        for j in range(len(c)-1, i, -1):
            if int(c[j][1]) < int(c[j-1][1]):
                c[j], c[j-1] = c[j-1], c[j]
    return c

def selection_sort(c):
    c = list(c)
    for i in range(len(c)):
        minj = i
        for j in range(i+1, len(c)):
            if int(c[j][1]) < int(c[minj][1]):
                minj = j
        c[i], c[minj] = c[minj], c[i]
    return c

input_num = int(input())
input_list = input().split()
bubble_list = bubble_sort(input_list)
selection_list = selection_sort(input_list)
for c in bubble_list:
    print(c, end='')
    if c != bubble_list[len(bubble_list)-1]:
        print(' ', end='')
print("\nStable")
stable_flg = True
for i in range(len(input_list)):
    if bubble_list[i] != selection_list[i]:
        stable_flg = False
    print(selection_list[i], end='')
    if i < len(input_list)-1:
        print(" ", end='')
if stable_flg:
    print("\nStable")
else:
    print("\nNot stable")