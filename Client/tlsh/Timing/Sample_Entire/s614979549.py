import sys

class Area:
    def __init__(self, start, end, area):
        self.start = start
        self.end = end
        self.area = area
    def addArea(self, area):
        self.area += area

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    
    area_stack = []
    field_stack = []
    
    for i in range(0, len(line)):
        c = line[i]
        if (c == "\\"):
            field_stack.append((c, i))
        elif (c == "/"):
            if len(field_stack) == 0:
                continue
            cc = field_stack.pop()
            current_area = Area(cc[1], i, (i - cc[1]))
            if len(area_stack) == 0:
                area_stack.append(current_area)
                continue
            prev_area = area_stack.pop()
            flag = True
            while (prev_area.start > current_area.start) and (prev_area.end < current_area.end):
                current_area.addArea(prev_area.area)
                if len(area_stack) == 0:
                    flag = False
                    break
                prev_area = area_stack.pop()
            if flag:
                area_stack.append(prev_area)
            area_stack.append(current_area)
    print str(reduce(lambda x, y: x + y, map(lambda x: x.area, area_stack), 0))
    s = ""
    s += str(len(area_stack)) + " "
    for item in area_stack:
        s += str(item.area) + " "
    s = s.strip()
    print s