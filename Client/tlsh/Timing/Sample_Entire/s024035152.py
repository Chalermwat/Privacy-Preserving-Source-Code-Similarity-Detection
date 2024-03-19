def area_cal(input_fig):
    stack = []
    # area = [[面積計算が始まった位置, 面積],・・・]
    area = []
    total = 0
    for i in range(len(input_fig)):
        fig = input_fig[i]
        if fig == "\\":
            stack.append(i)
        elif fig == "/" and stack:
            j = stack.pop()
            width = i - j
            total += width
            while area and area[-1][0] > j:
                width += area[-1][1]
                area.pop()
            area.append([i,width])
    return area, total
            
input_fig = input()
area, total = area_cal(input_fig)
print(total)
if area:
    print(len(area),*list(zip(*area))[1])
else:
    print(0)
