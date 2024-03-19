#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function
import time
import sys
import io
import re
import math
start = time.clock()

def bubble(cards):
    for i in range(len(cards)):
        for j in range(len(cards)-1, i, -1):
            if cards[j][1]<cards[j-1][1]:
                cards[j],cards[j-1]=cards[j-1],cards[j]

def selection(cards):
    for i in range(len(cards)):
        mini=i
        for j in range(i,len(cards)):
            if cards[j][1]<cards[mini][1]:
                mini=j
        cards[i],cards[mini]=cards[mini],cards[i]

def stable_test(orders,cards):
    for order in orders:
        n=-1
        for c in order:
            p=n
            n=cards.index(c)
            if p>n:
                return False
    return True

sys.stdin.readline()
data1=sys.stdin.readline().split()
data2=data1[:]
orders=[[c for c in data1 if c.endswith(str(i))] for i in range(1,10)]
orders=[o for o in orders if len(c)>1]

bubble(data1)
print(*data1)
print('Stable' if stable_test(orders, data1) else 'Not stable')

selection(data2)
print(*data2)
print('Stable' if stable_test(orders, data2) else 'Not stable')