sectional_view = input()

list_index_down = []
list_index_area_left = []
list_area = []


for index_now, mark in enumerate(sectional_view):
    if   mark == "\\":
        list_index_down += [index_now]
    elif mark == "/" and list_index_down:
        index_down_last = list_index_down.pop()
        area = index_now - index_down_last

        while ((list_index_area_left) and
               (list_index_area_left[-1] > index_down_last)):
            area += list_area.pop()
            list_index_area_left.pop()

        list_index_area_left.append(index_down_last)
        list_area.append(area)


print(sum(list_area))
print(len(list_area),*(list_area))

