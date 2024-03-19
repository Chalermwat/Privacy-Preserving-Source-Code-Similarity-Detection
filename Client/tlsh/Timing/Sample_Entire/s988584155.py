arr = list(input())
down = list()
areas = list()

for i, el in enumerate(arr):
    if el == "\\":
        down.append(i)
    elif el == "/" and not len(down) == 0:
        start_ind = down.pop()
        area = i - start_ind
        while len(areas) > 0 and areas[-1][0] > start_ind:
            area += areas.pop()[1]
        areas.append((start_ind, area))
    # print("LOOP: {}".format(i))
    # print("DOWN INDICES")
    # print(down)
    # print("AREAS")
    # print(areas)
    # print()

areas = [areas[i][1] for i in range(len(areas))]
print(sum(areas))
if len(areas) == 0:
    print("0")
else:
    print(len(areas), " ".join(map(str,areas)))
