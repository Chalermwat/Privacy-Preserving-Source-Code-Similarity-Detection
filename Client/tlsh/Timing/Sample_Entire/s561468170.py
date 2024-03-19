import sys
input = sys.stdin.readline

area_data = input()
total_area = 0
temp_area = 0

stack1 = []
stack2 = []

now_position = 0
for c in area_data:
    if c == '\\':
        stack1.append(now_position)
    elif c == '/':
        if len(stack1) > 0:
            last_potision = stack1.pop()
            temp_area = (now_position - last_potision)
            total_area += temp_area  # 前の\からの距離が、そのまま面積になる

            # print("before stack:{}".format(stack2))
            while len(stack2) > 0:
                prev_spot = stack2.pop()
                # print("prev spot:{}".format(prev_spot))
                # print("last_potision:{}".format(last_potision))
                if prev_spot[0] > last_potision:
                    temp_area += prev_spot[1]
                else:
                    stack2.append(prev_spot)
                    break

            stack2.append((last_potision, temp_area))

        # print("stack2:{}".format(stack2))

    now_position += 1

print(total_area)
print(len(stack2), end="")
for s in stack2:
    print(" ", end="")
    print(s[1], end="")
print()

