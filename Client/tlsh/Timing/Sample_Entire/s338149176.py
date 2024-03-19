from collections import deque
def calculate_area(lines):
    q = deque()
    partial_area = 0
    areas = []
    total_area = 0
    for i, line in enumerate(lines):
        if line == "\\":
            q.append(i)
        elif line == "/":
            if q:
                num = q.pop()
                partial_area = i - num
                total_area += partial_area
                for p_area in areas[::-1]:
                    if p_area[0] > num:
                        partial_area += areas.pop()[1]
                    else:
                        break
                areas.append([num, partial_area])
    areas_strigified = [str(v) for i, v in areas]
    print(total_area)
    if total_area:
        print("{} {}".format(len(areas), ' '.join(areas_strigified)))
    else:
        print(0)
                    

if __name__ == "__main__":
    data = input()
    calculate_area(data)
