string = input()
height = 0
height_list = [[0, False]]
for s in string:
    if s == '\\':
        height += -1
    elif s == '/':
        height += 1
    else:
        pass
    height_list.append([height, False])

highest = 0
for i in range(1, len(height_list)):
    if height_list[i-1][0] < height_list[i][0] <= highest:
        height_list[i][1] = True
    highest = max(highest, height_list[i][0])

puddles = []
area = 0
surface_level = None

for i in range(len(height_list)-1, -1, -1):
    if surface_level != None:
        area += surface_level - height_list[i][0]
        if surface_level == height_list[i][0]:
            puddles += [area]
            surface_level = None
            area = 0
    if surface_level == None and height_list[i][1]:
        surface_level = height_list[i][0]

puddles = puddles[::-1]
print(sum(puddles))
print(len(puddles), *puddles)
