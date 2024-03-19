import collections


def main():
    s = input()
    downs = collections.deque()
    pools = collections.deque()
    total_area = 0
    for now, char in enumerate(s):
        if char == "\\":
            downs.append(now)
        elif downs and char == "/":
            down = downs.pop()
            sub_area = now - down
            total_area += sub_area
            if not pools:
                pools.append((down, sub_area))
            else:
                while pools and down < pools[-1][0]:
                    sub_area += pools.pop()[1]
                pools.append((down, sub_area))
    print(total_area)
    pools = list(zip(*pools))[1] if pools else []
    print(len(pools), *pools)


if __name__ == '__main__':
    main()

