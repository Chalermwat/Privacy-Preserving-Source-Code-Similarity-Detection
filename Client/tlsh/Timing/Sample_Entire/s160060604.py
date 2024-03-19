if __name__ == "__main__":
    inp = input()
    a = []
    ans = []
    total = 0
    for i in range(len(inp)):
        if inp[i] == "\\":
            a.append(i)
        elif inp[i] == "/":
            if len(a) != 0:
                x = a.pop()
                d = i - x
                total += d
                while len(ans) != 0 and ans[-1][0] > x:
                    d += ans[-1][1]
                    ans.pop()
                ans.append([x, d])
    print(total)
    if total == 0:
        print(0)
    else:
        print(str(len(ans))+" "+(" ".join(map(str, [x[1] for x in ans]))))