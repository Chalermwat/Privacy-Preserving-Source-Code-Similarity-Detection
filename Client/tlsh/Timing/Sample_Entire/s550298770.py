def calc(list):
    #print list
    d = 0
    a = 0.0
    for c in list:
        if c == "\\":
            d += 1
            a += d - 1 + 0.5
        elif c == "_":
            a += d
        else:
            a += d - 1 + 0.5
            d -= 1
    return a

if __name__ == "__main__":
    line = raw_input()
    areas = []
    mode = False
    d = 0
    edge = 0
    for i in range(len(line)):
        #print i, line[i], d, edge, mode
        c = line[i]
        if mode:
            if c == "\\":
                d += 1
            elif c == "/":
                d -= 1
                if d == 0:
                    areas.append(calc(line[edge:i + 1]))
                    mode = False
        else:
            if c == "\\":
                d += 1
                edge = i
                mode = True
            elif c == "_":
                edge = i
            else:
                edge = i

    last = len(areas)
    high = edge
    if d != 0:
        d = 0
        edge = len(line) - 1
        mode = False
        for i in range(len(line) - 1 , high - 1, -1):
            #print i, line[i], d, edge, mode
            c = line[i]
            if mode:
                if c == "/":
                    d += 1
                elif c == "\\":
                    d -= 1
                    if d == 0:
                        #print i, edge
                        areas.insert(last, calc(line[i:edge + 1]))
                        mode = False
            else:
                if c == "/":
                    d += 1
                    edge = i
                    mode = True
                elif c == "_":
                    edge = i
                else:
                    edge = i

    if len(areas) == 0:
        print 0
        print 0
    else:
        areas = map(int, areas)
        print sum(areas)
        print len(areas),
        for i in range(len(areas) - 1):
            print areas[i],
        print areas[len(areas) - 1]