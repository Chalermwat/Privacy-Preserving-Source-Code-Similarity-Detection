import sys,itertools
from collections import deque

input = sys.stdin.readline


def _main():
    IN = input()
    area = 0
    all_area_stack = deque([])
    local_spot_stack = deque([])
    for i, op in enumerate(IN):
        if(op == '\\'):
            all_area_stack.append(i)
        elif(op == '/' and len(all_area_stack) > 0):
            i_p = all_area_stack.pop()
            area += (i - i_p)
            local_area = i - i_p
            while(len(local_spot_stack) > 0 and local_spot_stack[-1][0] > i_p):
                top_i, top_area = local_spot_stack.pop()
                local_area += top_area
            local_spot_stack.append((i, local_area))
    
    spots = [str(spot[1]) for spot in local_spot_stack]
    str_spots = ' '.join(spots)
    print(area)
    if(len(local_spot_stack) > 0):
        print('{} {}'.format(len(local_spot_stack), str_spots))
    else:
        print(0)





if __name__ == "__main__":
    _main()
