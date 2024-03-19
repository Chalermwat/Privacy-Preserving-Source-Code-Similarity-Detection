l = input()

stack1 = []
stack2 = []

all_area = 0

for val in range(len(l)):
    if l[val] == "\\":
        stack1.append(val)
    elif l[val] == "/" and stack1 != []:
        temp = stack1.pop(-1)
        all_area = all_area + (val - temp)
        each_area = val - temp
        while stack2 != [] and stack2[-1][0] > temp:
            each_area = each_area + stack2.pop(-1)[1]

        stack2.append([temp, each_area])
    else:
        pass

print(all_area)
print(len(stack2), end="")

for i in range(len(stack2)):
    print(" ", end="")
    print(stack2[i][1],end="")

print("")

