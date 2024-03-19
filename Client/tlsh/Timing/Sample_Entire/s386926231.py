lines = list(input())
total = 0
size = 0

stack = []
ponds = []
size = 0
for i in range(len(lines)):
    if lines[i] == "\\":
        stack.append(i)
    elif lines[i] == "/":
        if not stack == []:
            left_index = stack.pop()
            size = i - left_index
            target_index = left_index
            
            #order is tricky
            while not ponds == [] and ponds[-1][0] > left_index:
                direct = ponds.pop()
                target_index = direct[0]
                size += direct[1]
            ponds.append([target_index,size])




ans = []
ans.append(len(ponds))
for _ in ponds:
    ans.append(_[1])

print(sum(ans[1:]))
print(" ".join(map(str,ans)))
