
if __name__ == "__main__":
    line = input()

    S1 = []
    S2 = []
    total = 0

    for k, v in enumerate(line):
        if v == '\\':
            S1.append(k)
        elif v == '/' and len(S1) > 0:
            left_pos = S1.pop()
            area = k - left_pos
            total += area

            while True:
                if len(S2) < 1 or S2[-1][0] < left_pos:
                    S2.append([left_pos, area])
                    break
                else:
                    btm_area = S2.pop()
                    area += btm_area[1]

    print(total)
    indiv = [str(v[1]) for v in S2]
    indiv.insert(0, str(len(S2)))
    print(' '.join(indiv))

