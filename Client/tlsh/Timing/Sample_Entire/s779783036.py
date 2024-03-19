from collections import deque

def area(map):
    total = 0
    s1 = deque()
    s2 = deque()
    for i in range(len(map)):
        if map[i] == "\\":
            s1.append(i)    # 右斜面の要素番号を格納
        elif len(s1) > 0 and map[i] == "/":
            old = s1.pop()  # 水面の高さ(仮)を取り出す
            tmp = 0
            while len(s2) > 0 and old < s2[-1][0]:
                tmp += s2.pop()[1]  # 水没地帯の面積を計算(横に輪切りにするイメージで下から計算)
            s2.append([old, tmp + i - old]) # s2[[水面の始点, 水没地帯の面積(水面以外の面積 + (水面の終点 - 水面の始点)]]

    # 合計の水没面積を計算
    for i in range(len(s2)):
        total += s2[i][1]
    print(total)

    if s2:
        print(len(s2), end=" ")
        for i in range(len(s2)):
            if i != len(s2)-1:
                print(s2[i][1], end = " ")
            else:
                print(s2[i][1])
    else:
        print(len(s2))


if "__main__" == __name__:
    map = input().rstrip()
    area(map)
