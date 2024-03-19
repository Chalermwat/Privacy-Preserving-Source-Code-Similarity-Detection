#  Areas on the Cross-Section Diagram

class depth_Char:
    ch = ""
    depth = 0

    def __init__(self,char,depth):
        self.ch = char
        self.depth = depth

    def __str__(self):

        return f"{self.ch}:{self.depth}"


string = input()

depth = 0
d_list = []
for ch in string:
    if ch == "\\":
        depth -= 1
        d_list.append(depth_Char(ch,depth))

    elif ch == "_":
        d_list.append(depth_Char(ch,depth))

    elif ch == "/":
        d_list.append(depth_Char(ch,depth))
        depth += 1

# print(*d_list)

lake_list = []  #池のリストを作る
bslash_dict = dict()
for i,d_ch in enumerate(d_list):

    if d_ch.ch == "\\":
        bslash_dict[d_ch.depth] = i
    elif d_ch.ch == "/" and d_ch.depth in bslash_dict:
        j = bslash_dict[d_ch.depth]

        is_need_append = True
        # print(f"search:{[j,i]}")
        remove_list = []  # foreachループの中では削除せず、最後にまとめて削除する

        for lake in lake_list:
            if is_need_append and lake[0] < j and i < lake[1]:
                is_need_append = False

            if j < lake[0] and lake[1] < i:
                # print(f"remove:{lake}")
                remove_list.append(lake)
        
        for rem in remove_list:
            lake_list.remove(rem)

        if is_need_append:
            lake_list.append([j,i])
        

lake_area_list = []
for i,j in lake_list:
    lake = string[i:j+1]
    t_depth = 0
    area = 0
    for ch in lake:
        if ch == "\\":
            t_depth += 1
            area += t_depth
        elif ch == "_":
            area += t_depth
        elif ch == "/":
            t_depth -= 1
            area += t_depth
    
    lake_area_list.append(area)

print(sum(lake_area_list))
print(len(lake_area_list),*lake_area_list)



