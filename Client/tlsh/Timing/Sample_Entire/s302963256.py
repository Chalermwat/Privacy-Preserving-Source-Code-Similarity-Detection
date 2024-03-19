# -*- coding: UTF-8 -*-
# Stack

top = 0
S = {}

def push(x):
    global top
    global S
    top += 1
    S[top] = x

def pop():
    global top
    global S
    top -= 1
    return S[top + 1]

input_list = list(input().split()) #計算対象（スペース区切り→配列に展開）

for target in input_list:
    if target == '+':
        a = pop()
        b = pop()
        c = b+a
        push(c)
    elif target == '-':
        a = pop()
        b = pop()
        c = b-a
        push(c)
    elif target == '*':
        a = pop()
        b = pop()
        c = b*a
        push(c)
    else:
        push(int(target))

print(pop())

