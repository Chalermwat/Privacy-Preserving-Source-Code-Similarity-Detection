from sys import stdin
from collections import deque

def main():
    point = 0
    watermarks = []
    ponds = []

    for mark in list(stdin.readline()):
        point += 1
        if mark == "\\":
            watermarks.append(point)
        elif mark == "/":
            if watermarks:
                start_point = watermarks.pop()
                area = point - start_point
                while ponds and ponds[-1][0] > start_point:
                    area += ponds.pop()[1]
                ponds.append((start_point, area))

    pond_list = [pond[1] for pond in ponds]
    print(sum(pond_list))
    print(len(pond_list), *pond_list)

main()
