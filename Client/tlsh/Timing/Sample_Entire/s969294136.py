# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_D&lang=jp
#  Areas on the Cross-Section Diagram : python3
#  2018.11.27 yonezawa


from collections import deque
import heapq
import sys
input = sys.stdin.readline


def main():
    q = deque()
    m = str(input()).strip()
    dq = []
    count = 0
    for i in range(len(m)):
        if (m[i] == "\\" ):
            q.append(i)
            continue
        if (m[i] == "/" and len(q) > 0):
            j = q.pop()
            count += i - j
            #dq.append((j,i))
            dq.append((j,i))
    print (count)
    if (len(dq) == 0):
        print (0)
        return

    l = []
    dq.sort()
    dq.reverse()
    (a,b) = dq.pop()
    
    score = b - a
    while len(dq) > 0:
        (i,n) = dq.pop()
        if ( b > i ):
            score += n - i
        else:
            l.append(score)
            score = n - i
            a = i
            b = n
    else:
        l.append(score)

    print (len(l),*l)

if __name__ == '__main__':
    main()
