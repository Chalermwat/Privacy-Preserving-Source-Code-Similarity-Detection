# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_D
sample_input = list(range(3))
# sample_input[0] = '''\\//'''
# sample_input[1] = '''\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/\'''
# sample_input[2] = ''''''

sample_input[0] = '''\\\\//'''
sample_input[1] = '''\\\\///\\_/\\/\\\\\\\\/_/\\\\///__\\\\\\_\\\\/_\\/_/\\'''
sample_input[2] = ''''''

give_sample_input = None
if give_sample_input is not None:
    sample_input_list = sample_input[give_sample_input].split('\n')
    def input():
        return sample_input_list.pop(0)
        
# main
# a list of tuples (h, l, r)
# h = the hight
# l, r = max of heights of points which is left (right) or equal to this point
terrain_data = []

str_input = input()
list_input = list(str_input)

height = 0
left_max_height = 0
terrain_data.append([height,left_max_height, None])
for path in list_input:
    if path == '/':
        height += 1
    elif path == '\\':
        height -= 1
    left_max_height = max(left_max_height, height)
    terrain_data.append([height,left_max_height, None])

right_max_height = None # dealt as negative infinity
for index in range(len(terrain_data)-1, -1, -1):
    height = terrain_data[index][0]
    if right_max_height is None:
        right_max_height = height
    else:
        right_max_height = max(right_max_height, height)
    terrain_data[index][2] = right_max_height

pool_left = -1
pool_right = -1
area = 0
areas = []
prev_depth = 0
for data in terrain_data:
    depth = min(data[1], data[2]) - data[0]
    area += (prev_depth + depth)/2
    if depth == 0:
        if pool_left < pool_right:
            areas.append(int(area))
            area = 0
        pool_right += 1
        pool_left = pool_right
    else:
        pool_right += 1
    prev_depth = depth

print(sum(areas))
output = str(len(areas)) + ' '
for a in areas:
    output += str(a) + ' '
print(output[:-1])