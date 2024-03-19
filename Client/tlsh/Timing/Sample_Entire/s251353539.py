class Flood:
    """
    begin : int
        水たまりの始まる場所
    area : int
        水たまりの面積
    """
    def __init__(self, begin, area):
        self.begin = begin
        self.area = area

down_index_stack = []  # \の場所
flood_stack = []  # (水たまりの始まる場所, 面積)


for i, c in enumerate(input()):
    if c == '\\':
        down_index_stack.append(i)
    if c == '/':
        if len(down_index_stack) >= 1:  # 現在の/に対応する\が存在したら

            l = down_index_stack.pop()  # 現在の水たまりの始まる場所
            area = i - l  # 現在の水たまりの現在の高さの部分の面積はi-l

            # 現在の水たまりが最後の水たまりを内包している間は
            # (現在の水たまりの始まる場所が最後の水たまりの始まる場所より前にある間は)
            while len(flood_stack) >= 1 and l < flood_stack[-1].begin:
                # 最後の水たまりを現在の水たまりに取り込む
                last_flood = flood_stack.pop()
                area += last_flood.area

            flood_stack.append(Flood(l, area))  # 現在の水たまりを最後の水たまりにして終了


area_list = [flood.area for flood in flood_stack]
print(sum(area_list))
print(' '.join(list(map(str, [len(area_list)] + area_list))))

