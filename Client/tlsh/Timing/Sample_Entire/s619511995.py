"""
O(n^2)??????????§£???
"""

danmen = input()
depth = []
tmp_dpt = 0

for line in danmen:
    depth.append(tmp_dpt)

    if line == "\\":
        tmp_dpt -= 1
    elif line == "/":
        tmp_dpt += 1

# len(depth) = len(danmen) + 1?????¨???
depth.append(tmp_dpt)

# print(depth)

i = 0
L = []

while i < len(danmen):
    if len(set(danmen[i:])) == 1:
        break

    if danmen[i] == "\\":
        if depth[i] in depth[i + 1:]:
            stack = 0
            area = 0

            for line in danmen[i:]:
                if line == "\\":
                    area += 1 + 2 * stack
                    stack += 1
                elif line == "/":
                    stack -= 1
                    area += 1 + 2 * stack
                else:
                    area += 2 * stack

                if stack == 0:
                    break

            if area != 0:
                L.append(area // 2)
                i += depth[i + 1:].index(depth[i])

    i += 1

print(sum(L))
print(len(L), *L)