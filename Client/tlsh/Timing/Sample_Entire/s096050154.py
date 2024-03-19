def cal_water(floods):
    fstack = []
    astack = []
    i = 0
    for flood in floods:
        if flood == '\\':
            fstack.append(i)
        elif flood == '/' and len(fstack) > 0:
            s = fstack.pop(-1)
            area = (i - s) * 1
            while len(astack) > 0 and astack[-1][0] > s:
                _, a = astack.pop(-1)
                area += a
            astack.append((s, area))   
        else:
            pass
        i += 1
    
    tot = 0
    tot_area = 0
    out = ''
    while len(astack) > 0:
        _, area = astack.pop()
        tot += 1
        tot_area += area
        out = ' ' + str(area) + out
    
    print(tot_area)
    print(str(tot) +  out)

if __name__ == '__main__':
    floods = input()
    cal_water(floods)
