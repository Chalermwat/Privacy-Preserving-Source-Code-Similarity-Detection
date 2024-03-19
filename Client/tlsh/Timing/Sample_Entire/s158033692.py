input_string = input()
total_area = 0
num_lake = 0
lake_areas = []

v_lakes = [] # (湖の始まりidx, 湖の面積)
idx_stack = [] #地形管理

for i, c in enumerate(input_string):
    if c == "\\":
        idx_stack.append(i)
    elif c == "/" and idx_stack:
        poped_i = idx_stack.pop()
        total_area += i - poped_i
        tmp_area = i - poped_i
        while v_lakes and v_lakes[-1][0] > poped_i:
            tmp_area += v_lakes.pop()[1]
            
        v_lakes.append((poped_i, tmp_area))
#print(v_lakes)

print(total_area)
ans = [area[1] for area in v_lakes] 
print(len(v_lakes), *ans)
