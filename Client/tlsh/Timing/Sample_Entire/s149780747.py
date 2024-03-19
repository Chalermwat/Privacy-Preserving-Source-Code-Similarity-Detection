# -*- coding:utf-8 -*-
import sys


def cross_section_diagram(diagram):
    stack = []
    area = []
    for i, ch in enumerate(diagram):
        if ch == "\\":
            stack.append(i)
        elif ch == "/":
            if stack:
                point = stack.pop()
                area.insert(0, (point, i - point))
        else:
            pass
    result = []
    if area:
        p1, cnt1 = area.pop(0)
        for p2, cnt2 in area:
            if p1 < p2:
                cnt1 += cnt2
            else:
                result.insert(0, cnt1)
                p1 = p2
                cnt1 = cnt2
        result.insert(0, cnt1)

    print(sum(result))
    result.insert(0, len(result))
    print(" ".join([str(n)for n in result]))
    return result


if __name__ == "__main__":
    diagram = [val for val in sys.stdin.read().splitlines()]
    cross_section_diagram(diagram[0])