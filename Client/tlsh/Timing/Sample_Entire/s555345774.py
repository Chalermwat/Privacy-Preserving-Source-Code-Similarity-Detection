#!/usr/bin/env python
#-*- coding: utf-8 -*-


def selection_sort(l):
    N = len(l)
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if int(l[j][1]) < int(l[minj][1]):
                minj = j
        if i != minj:
            l[i], l[minj] = l[minj], l[i]


def bubble_sort(l):
    N = len(l)
    for i in range(0, N):
        for j in range(N - 1, i, -1):
            if int(l[j][1]) < int(l[j - 1][1]):
                l[j], l[j - 1] = l[j - 1], l[j]
    pass


if __name__ == '__main__':
    N = raw_input()
    l1 = raw_input().split()
    l2 = l1[:]
    bubble_sort(l1)
    print ' '.join(l1)
    print "Stable"
    selection_sort(l2)
    print ' '.join(l2)
    if l1 == l2:
        print "Stable"
    else:
        print "Not stable"
