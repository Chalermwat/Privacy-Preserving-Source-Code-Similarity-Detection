def main():
    line = input()
    s1 = []
    s2 = []
    sum = 0
    for i, s in enumerate(line):
        if s == "\\":
            # 谷の位置をスタックに積む
            s1.append(i)
        elif s == "/" and len(s1) > 0:
            # 山で対応する谷があるなら、面積に追加
            j = s1.pop()
            sum += i - j  # 谷から山の距離を水たまりの面積に追加
            # jより前に位置する水たまりの面積を追加
            a = i - j
            while len(s2) > 0 and s2[-1][0] > j:
                a += s2.pop()[1]
            # (水たまりの左端の位置, 水たまりの面積)のタプルをスタックに積む
            s2.append((j, a))

    print(sum)
    print(len(s2), end="")
    for x in s2:
        print(f" {x[1]}", end="")
    print()


if __name__ == "__main__":
    main()

