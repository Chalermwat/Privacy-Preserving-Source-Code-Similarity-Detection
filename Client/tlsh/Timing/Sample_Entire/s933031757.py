"""
# 標準入力取得
## 文字列
 = sys.stdin.readline().rstrip()
 = list(sys.stdin.readline().rstrip())

## 数値
 = int(sys.stdin.readline())
 = map(int, sys.stdin.readline().split())
 = list(map(int, sys.stdin.readline().split()))
 = [list(map(int,list(sys.stdin.readline().split()))) for i in range(h)]  # 二次元配列入力　二次元マップみたいな入力のとき

# 0埋め, 小数点出力桁指定時のときの出力
a = 100
b = 0.987654321
print("{0:06d}-{1:6f}".format(a,b))
000100-0.987654

# 文字列をリストに格納
char_list = list("abcd") # ["a","b","c","d"]
"""

import math
import sys
import itertools
import queue
from fractions import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

mod = 1000000007

if __name__ == "__main__":
    s=[]#"\\"のindexが入るスタック
    p=[]#popしたindexと面積のタプルが入るスタック
    i=0#index番号
    a=0#
    for c in input():
        if "\\"==c:#"\"だと認識できない仕様
            s+=[i]#index番号の取得とスタックへの挿入
        elif "/" ==c and s:#index番号が空の時はやらない
            j=s.pop()#末尾のindex番号を取得して削除
            t=i-j
            a+=t
            while p and p[-1][0]>j:
                t+=p[-1][1];
                p.pop()
            p+=[(j,t)]
        i+=1
    print(a)
    if p:
        print(len(p),*list(zip(*p))[1])
    else:
        print(0)
