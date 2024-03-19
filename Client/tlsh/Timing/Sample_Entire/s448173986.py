from collections import deque
import sys
input = sys.stdin.readline

def putsarray(array):
    if len(array) == 0:
        print()
        return
    for i in range(len(array) - 1):
        print(int(array[i]), end=' ')
    print(int(array[-1]))

def main():
    stack = deque([])
    instr = input()
    is_same_lake = False
    result = 0

    lakes = deque([])

    for i in range(len(instr)):
        char = instr[i]
        if char == "\\":
            stack.append(i)
        elif char == "_":
            pass
        elif char == "/":
            if len(stack) == 0:
                is_same_lake = False
                continue
            down = stack.pop()
            result += i - down
            lake_area = i - down
            index = len(lakes) -1
            while True:
                if index < 0:
                    break
                lake = lakes[index]
                if down < lake[0] and lake[1] < i:
                    lake_area += lakes.pop()[2]
                else:
                    break
                index -= 1
                    
            lakes.append((down, i, lake_area))

    print(int(result))
    putsarray([len(lakes),] + [l[2] for l in lakes])

    

main()




