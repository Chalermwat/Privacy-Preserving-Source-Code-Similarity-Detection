from collections import deque
input_list = list(input())

left_idx_stack = deque()
puddle_stack = deque()

for idx, s in enumerate(input_list):
    if s == "\\":
        left_idx_stack.append(idx)
    
    elif s == '/':
        if left_idx_stack:
            latest_left_idx = left_idx_stack.pop()
            area = idx - latest_left_idx
        
            if not puddle_stack:
                puddle_stack.append((latest_left_idx, area))
            
            elif latest_left_idx > puddle_stack[-1][0]:
                puddle_stack.append((latest_left_idx, area))
            else:
                
                while len(puddle_stack) != 0 and (latest_left_idx < puddle_stack[-1][0]):
                    latest_puddle = puddle_stack.pop()
                    area += latest_puddle[1]
                    
                puddle_stack.append((latest_left_idx, area))
        else:
            pass
areas = [p[1] for p in puddle_stack]
print(sum(areas))
print(len(areas), *areas)

