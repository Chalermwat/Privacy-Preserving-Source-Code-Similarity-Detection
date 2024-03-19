import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    S = input()
    pair = []
    stack = [('%',-1)]
    for j,s in enumerate(S):
        if s == '/':
            if stack[-1][0] == '\\':
                i = stack[-1][1]
                stack.pop()
                pair.append((i,j))
        elif s == '_':
            continue
        else:
            stack.append((s,j))
    
    pond = []
    tot = 0
    k = len(pair) - 1
    while  k >= 0:
        fin = pair[k][0] - 1
        area = 0
        while k >= 0 and fin < pair[k][0]:
            area += pair[k][1] - pair[k][0]
            k -= 1
        pond.append(area)
        tot += area
    pond.append(len(pond))

    print(tot)
    print(*pond[::-1])
if __name__ == '__main__':
    main()
