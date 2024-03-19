#!/usr/bin/env python3
import sys


def solve(S: int):
    def divisor(n): #nの約数を全て求める

        i = 1
        while i * i <= n:
            if n%i == 0:
                if 0<= i <= 10**9 and 0 <= n//i <=10**9:
                    return i
            i += 1
    # 0 0 a b c d

    if int(S**(1/2))**2 == S:
        half  =int(S**(1/2))
        b = c = 0
    else:
        half = int(S**(1/2))+1
        res = half**2-S
        num = divisor(res)
        b = num
        c = res//num

    a = d = half 

    print(0,0,a,b,c,d)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = int(next(tokens))  # type: int
    solve(S)

if __name__ == '__main__':
    main()
