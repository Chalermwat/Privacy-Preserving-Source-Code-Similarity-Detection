downhill_stack = []
idx_area_stack = []
for idx, c in enumerate(input()):
    if c == '\\':
        downhill_stack.append(idx)
    elif c == '/' and len(downhill_stack) > 0:
        downhill_idx = downhill_stack.pop()
        current_level_area = idx - downhill_idx
        if len(idx_area_stack) == 0:
            idx_area_stack.append((downhill_idx, current_level_area))
            continue
        last_idx = idx_area_stack[-1][0]
        if downhill_idx < last_idx:
            prov_area = current_level_area
            while downhill_idx < last_idx:
                idx_area = idx_area_stack.pop()
                prov_area += idx_area[1]
                if len(idx_area_stack) == 0:
                    break
                last_idx = idx_area_stack[-1][0]
            prov_idx_area = (downhill_idx, prov_area)
            idx_area_stack.append(prov_idx_area)
        else:
            idx_area_stack.append((downhill_idx, current_level_area))
puddle_num = len(idx_area_stack)
areas = list(map(lambda x: x[1], idx_area_stack))
print(sum(areas))
if puddle_num > 0:
    print(puddle_num, " ".join(map(str, areas)))
else:
    print(puddle_num)
