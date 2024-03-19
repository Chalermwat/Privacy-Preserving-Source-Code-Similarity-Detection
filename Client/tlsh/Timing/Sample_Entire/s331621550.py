def main():
    S = input()

    def an_area(S):
        ans = 0
        stack_in = []
        stack_out = []
        for i,ch in enumerate(S):
            if ch == '\\':
                stack_in.append(i)
            elif stack_in and ch == '/':
                j = stack_in.pop()
                cur =  i - j
                stack_out.append((j,i,cur))
                ans += cur
        return ans,stack_out

    ans, l = an_area(S)
    if ans == 0:
        print(ans)
        print(len(l))
        return

    l.sort()
    pre_le, pre_ri = l[0][0], l[0][1]
    pre_ar = 0
    areas = []
    for le,ri,ar in l:
        if pre_le <= ri <= pre_ri:
            pre_ar += ar
        else:
            areas.append(pre_ar)
            pre_ar = ar
            pre_le, pre_ri = le, ri
    else:
        areas.append(pre_ar)
    
    print(ans)
    print(len(areas),*areas)

if __name__ == '__main__':
    main()
