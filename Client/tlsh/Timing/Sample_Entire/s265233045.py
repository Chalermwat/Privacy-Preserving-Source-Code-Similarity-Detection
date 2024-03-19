target = input()
now_height = []
now_area = [0]
answer = []
continued = 0
depth = 0
depth_list = []
for t in target:
    # print(now_height,depth_list,now_area,answer,continued)
    if t == '\\':
        now_height.append(continued)
        depth_list.append(depth)
        now_area.append(0)
        depth -= 1
    elif t == '_':
        pass
    elif t == '/' and len(now_height) > 0:
        depth += 1
        started = now_height.pop()
        temp_area = continued - started
        # print(depth_list[-1],depth)
        now_area[-1] += temp_area
        if depth > depth_list[-1]:
            while depth > depth_list[-1]:
                temp = now_area.pop()
                now_area[-1] += temp
                depth_list.pop()
    continued += 1
now_area = list(filter(lambda x:x != 0,now_area))
answer.extend(now_area)
print(sum(answer))
print(len(answer),*answer)