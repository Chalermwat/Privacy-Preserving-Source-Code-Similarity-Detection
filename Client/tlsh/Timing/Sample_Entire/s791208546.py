from collections import deque

S = input()

bs_idx = deque()
areas = []
for idx, s in enumerate(S):
    if s == "\\":
        bs_idx.append(idx)
    if s == "/":
        if bs_idx:
            left_idx = bs_idx.pop()
            areas.append([left_idx, idx - left_idx])

areas.sort()

if not areas:
    print(0)
    print(0)
else:
    ans = []
    i = 0
    while True:
        if i == len(areas):
            break
        area = areas[i][1]
        tmp = areas[i][0] + area
        while True:
            i += 1
            if i != len(areas) and areas[i][0] < tmp:
                area += areas[i][1]
            else:
                ans.append(area)
                break

    print(sum(ans))
    print(len(ans), " ".join(map(str, ans)))

