def main():
    """ ????????? """
    S1 = [] # ????????????1(??????????????????)
    S2 = [] # ????????????2(??????????°´????????????????????¨??¢???)
    A = 0 # ?????¢???

    inp = input()
    #inp = "\\\\///\\_/\\/\\\\\\\\/_/\\\\///__\\\\\\_\\\\/_\\/_/\\"
    for i in range(len(inp)):
        if inp[i] == chr(0x5c): # \ 
            S1.append(i)
            S2.append([i,0])
        elif inp[i] == chr(0x2f): # /
            if len(S1):
                j = S1.pop()
                d = i - j
                A += d
                k = d
                while len(S2):
                    p = S2.pop()
                    if p[1] > 0:
                        k += p[1]
                    else:
                        S2.append([p[0],k])
                        break
        #print("[{}] {} A={} S1:{} S2:{}".format(i,inp[i],A,S1,S2))
    L = []
    for p in S2:
        if p[1] > 0:
            L.append(p[1])
    print(A)
    if A > 0:
        print("{} {}".format(len(L)," ".join(map(str,L))))
    else:
        print("0")


if __name__ == '__main__':
    main()