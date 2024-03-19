a = input().strip()
stack = []
area = 0
area_list = []

for i, slope in enumerate(a):
    if slope == '\\':
        stack.append(i)
    elif slope == '/' and len(stack) != 0:
        ip = stack.pop(len(stack)-1)
        area += (i - ip)
        a = i - ip
        while len(area_list) != 0 and area_list[len(area_list)-1][0] > ip:
            temp = area_list.pop(len(area_list)-1)
            a += temp[1]
        area_list.append([ip, a])
    
print(area)
print('{}'.format(len(area_list)), end='')
if len(area_list) != 0:
    print(' ', end='')
print(' '.join([str(i[1]) for i in area_list]))
    
