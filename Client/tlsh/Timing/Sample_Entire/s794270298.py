# -*- coding: utf-8 -*-

def main():
    down_positions = []
    ponds = []
    for index, value in enumerate(raw_input()):
        if value == '\\':
            down_positions.append(index)
        elif value == '/' and down_positions:
            right = index
            left = down_positions.pop()
            area = right - left
            # candidate_pond = []
            area2 = 0
            while ponds and left < ponds[-1][0]:
               # candidate_pond.append(ponds.pop(-1))
               area2 += ponds.pop(-1)[1]

            # new_pond = (left, area + sum([x[1] for x in candidate_pond]))
            new_pond = (left, area + area2)
            ponds.append(new_pond)
    
    print sum(x[1] for x in ponds)
    print len(ponds), 
    for pond in ponds:
        print pond[1], 

if __name__ == '__main__':
    main()