from collections import deque

if __name__ == "__main__":
    slopes = input()
    total_area = 0
    slope_queue = deque()
    area_queue = deque()

    for i, slope in enumerate(slopes):
        if slope == '\\':
            slope_queue.append(i)
        elif slope == '/' and len(slope_queue) != 0:
            target = slope_queue.pop()
            area = i - target
            total_area += area
            if len(area_queue) == 0:
                area_queue.append((target, area))
            else:
                temp_area = area
                while True:
                    target_area = area_queue.pop()
                    if target < target_area[0]:
                        temp_area += target_area[1]
                        if len(area_queue) == 0:
                            area_queue.append((target, temp_area))
                            break
                    else:
                        area_queue.append(target_area)
                        area_queue.append((target, temp_area))
                        break

    print(total_area)
    if len(area_queue) == 0:
        print(len(area_queue), end='\n')
    else:
        print(len(area_queue), end=' ')
    for i, area in enumerate(area_queue):
        if i < len(area_queue) - 1:
            print(area[1], end=' ')
        else:
            print(area[1], end='\n')
