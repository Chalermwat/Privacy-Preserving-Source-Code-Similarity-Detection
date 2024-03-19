current_l = 0
stack_s = []
stack_each_area = []
areas = []
for s in input():
#     print(stack_each_area)
    if(s == '\\'):
        stack_s.append(current_l)
    elif(s == '/'):
        if(len(stack_s)==0):
            continue
        left_edge = stack_s.pop(-1)
        area = current_l - left_edge
        areas.append(area)
        
        merged_area = area
        merged_j = []
        for j in range(len(stack_each_area)):
            if( left_edge < stack_each_area[j][0] and stack_each_area[j][0] < current_l):
                merged_area += stack_each_area[j][1]
                merged_j.append(j)
        for del_j in merged_j[::-1]:
            del stack_each_area[del_j]
        stack_each_area.append((current_l, merged_area))
    current_l += 1
print(sum(areas))
if(len(stack_each_area) != 0):
    print(len(stack_each_area), " ".join([ str(lm[1]) for lm in stack_each_area]))
else:
    print(0)
