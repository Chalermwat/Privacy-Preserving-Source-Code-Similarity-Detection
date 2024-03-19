#インプットdata
input_data = input()

#初期値
stack_list = list()
area_list = list()
area_sum = 0

#計算の実行
for i in range(len(input_data)):
    if input_data[i] == "\\":
        stack_list.append(i)
    elif len(stack_list) > 0 and input_data[i] == "/":
        temp_area = i - stack_list[-1]
        area_sum += temp_area
        if len(area_list) == 0 or area_list[-1][0] < stack_list[-1]:
            area_list.append([stack_list[-1], temp_area])
        else:
            area_list[-1][0] = stack_list[-1]
            area_list[-1][1] += temp_area
            temp_len = len(area_list)
            for j in range(temp_len-1, 0, -1):
                if area_list[j-1][0] > area_list[j][0]:
                    area_list[j-1][0] = area_list[j][0]
                    area_list[j-1][1] += area_list[j][1]
                    del area_list[j]
                else:
                    break
        del stack_list[-1]

#結果の表示
print(area_sum)
print(len(area_list), end="")
for i in range(len(area_list)):
    print(f" {area_list[i][1]}", end="")
print("")

