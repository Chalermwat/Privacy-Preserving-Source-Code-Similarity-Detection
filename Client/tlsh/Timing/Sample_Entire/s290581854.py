# -*- coding: utf-8 -*-

def main():
    input_string = raw_input().strip()
    down_positions = []
    ponds = []
    for index, value in enumerate(input_string):
        if value == '\\':
            down_positions.append(index)
        elif value == '/' and down_positions:
            right = index
            left = down_positions.pop()
            area = right - left
            candidate_pond = []
            while ponds and left < ponds[-1][0]:
               candidate_pond.append(ponds.pop(-1))

            new_pond = (left, area + sum([x[1] for x in candidate_pond]))
            ponds.append(new_pond)
    
    print sum(x[1] for x in ponds)
    print len(ponds), 
    for pond in ponds:
        print pond[1], 

if __name__ == '__main__':
    main()