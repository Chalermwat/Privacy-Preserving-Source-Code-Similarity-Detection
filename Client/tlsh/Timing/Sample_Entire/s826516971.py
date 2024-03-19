# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 14:04:29 2018
ALDS1-3a
@author: maezawa
"""
maxn=200
s = input().split()
st = [0 for _ in range(maxn)]
top = 0

for i in range(len(s)):
    c = s.pop(0)
    if c == '+':
        b = st[top]
        top -= 1
        a = st[top]
        top -= 1
        ans = a + b
        top += 1
        st[top] = ans
    elif c == '-':
        b = st[top]
        top -= 1
        a = st[top]
        top -= 1
        ans = a - b
        top += 1
        st[top] = ans
    elif c == '*':
        b = st[top]
        top -= 1
        a = st[top]
        top -= 1
        ans = a * b
        top += 1
        st[top] = ans
    else:
        top += 1
        st[top] = int(c)
print(st[top])
