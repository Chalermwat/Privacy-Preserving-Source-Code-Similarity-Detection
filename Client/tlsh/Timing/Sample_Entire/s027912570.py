landform = [c for c in input()]
down = []
areas = []

for i in range(len(landform)):
    if landform[i] == '\\':
        down.append(i)
    if landform[i] == '/':
        if down:
            pair = down.pop()
            area = i - pair
            while areas and areas[-1][0] > pair:
                area += areas.pop()[1]
            areas.append([pair, area])

sum_area = 0
for area in areas:
    sum_area += area[1]
print(sum_area)

ans = []
ans.append(str(len(areas)))
ans += [str(area[1]) for area in areas]

print(' '.join(ans))

