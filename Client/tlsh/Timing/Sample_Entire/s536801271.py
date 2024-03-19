from collections import deque


def main():
    total = 0
    s1 = deque()
    s2 = deque()
    str = input()
    for i in range(len(str)):
        if str[i] == "\\":
            s1.append(i)
        elif len(s1) > 0 and str[i] == "/":
            old = s1.pop()
            tmp = 0
            while len(s2) > 0 and old < s2[-1][0]:
                tmp += s2.pop()[1]
            s2.append([old, tmp + i - old])

    for i in range(len(s2)):
        total += s2[i][1]
    print(total)
    if s2:
        print(len(s2), end="")
        for i in range(len(s2)):
            if i == len(s2) - 1:
               print(" {}".format(s2[i][1]))
            else:
               print(" {}".format(s2[i][1]), end="")
    else:
        print(len(s2))

if __name__ == '__main__':
    main()

