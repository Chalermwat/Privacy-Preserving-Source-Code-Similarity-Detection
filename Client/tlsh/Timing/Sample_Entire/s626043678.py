from collections import deque

input_list = input()
area = 0
depth_arr = deque()
area_arr = deque()

for i, input_str in enumerate(input_list):
    if "\\" == input_str:
        depth_arr.append(i)
    elif "/" == input_str:
        if len(depth_arr):
            position = depth_arr.pop()
            pool = i - position
            area += pool

            while len(area_arr):
                pre_position, pre_pool = area_arr.pop()
                if position <= pre_position:
                    pool += pre_pool
                else:
                    area_arr.append((pre_position, pre_pool))
                    break
            area_arr.append((position, pool))

areas = 0
for pos, pool in area_arr:
    areas += pool
print(areas)
print(len(area_arr), *[list[1] for list in area_arr])