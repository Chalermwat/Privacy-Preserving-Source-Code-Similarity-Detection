from collections import deque
import sys


def func(S):
    i = 0
    water = 0
    stack = []
    waters = []
    while i < len(S):
        for inc, s in enumerate(S[i:]):
            if s == '\\':
                stack.append(s)
                water += len(stack)

            if not stack:
                break

            if s == '/':
                stack.pop()
                water += len(stack)

            if s == '_':
                water += len(stack)

            if not stack:
                break
        if water != 0 and not stack:
            waters.append(water)
        water = 0

        if inc == len(S[i:]) - 1:
            if not stack:
                i = len(S)
            break

        i += inc if inc else 1

    return waters, S[i:]


if __name__ == '__main__':
    S = [c for c in input()]

    waters, S = func(S)

    rev_S = []
    for s in S[::-1]:
        if s == '\\':
            rev_S.append('/')
        elif s == '/':
            rev_S.append('\\')
        else:
            rev_S.append('_')

    new_waters, _ = func(rev_S)
    waters += new_waters[::-1]

print(sum(waters))
print(len(waters), *waters)

