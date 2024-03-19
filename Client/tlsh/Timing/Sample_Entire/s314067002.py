
from collections import deque

def main():
    s1 = deque()
    s2 = deque()
    total = 0

    string = input()

    for i in range(len(string)):
        if string[i] == '\\':
            s1.append(i)
        elif string[i] == '/' and len(s1) > 0:
            j = s1.pop()
            a = i - j
            total += a

            while (len(s2) > 0 and s2[-1][0] > j):
                a += s2[-1][1]
                s2.pop()

            s2.append((j, a))

    ans = []
    while (len(s2) > 0):
        ans.append(s2[-1][1])
        s2.pop()

    print(total)

    print(len(ans), *ans[::-1])

if __name__ == "__main__":
    main()