def main():
    SS = 0
    s1 = []
    s2 = []
    l = raw_input()
    for b in range(len(l)):
        c = l[b]
        if c == '\\':
            s1.append(b)
        elif c == "/":
            if not len(s1) == 0:
                a  = s1.pop()
                s  = b-a
                SS += s
                while not len(s2) == 0:
                    sigma,alpha,beta = s2.pop()
                    if alpha>a and beta<b:
                        s = s + sigma
                    else:
                        s2.append([sigma,alpha,beta])
                        break
                s2.append([s,a,b])
        
    print SS
    print len(s2),
    for item in s2[:-1]:
        print item[0],
    if not len(s2) == 0:
        print s2[-1][0]


if __name__ == "__main__":
    main()