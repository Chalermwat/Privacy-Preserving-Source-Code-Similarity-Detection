from collections import deque

if __name__ == '__main__':
    s = input()
    s1 = deque()
    s2 = deque()
    summ = 0
    for i, c in enumerate(s):
        if c == '\\':
            s1.append(i)
        elif s[i] == '/' and len(s1) > 0:
            j = s1.pop()
            summ += i-j
            a = i-j
            while len(s2) > 0 and s2[-1][0] > j:
                a+= s2.pop()[1]
            s2.append([j, a])
    
    ans = []
    while len(s2) > 0:
        ans.append(s2.pop()[1])
    ans.reverse()
    print(sum(ans))
    counter = len(ans)
    ans.insert(0, counter)
    a = list(map(str, ans))
    print(' '.join(a))
