import sys
input = sys.stdin.readline

cs_view = input().rstrip('\r\n')
list_v = list(cs_view)

stack1 = []
all_sum = 0
sum_stack = []
for i, elem in enumerate(list_v):
    if elem == '\\':
        stack1.append(i)
    elif len(stack1) > 0 and elem == '/':
        j = stack1.pop()
        all_sum += i - j
        a = i - j
        while len(sum_stack) > 0 and sum_stack[-1][0] > j:
            a += sum_stack.pop()[1]
        sum_stack.append([j, a])

print(all_sum)
esum = []
for a in sum_stack:
    esum.append(a[1])
esum.insert(0, len(esum))
maped_esum = map(str, esum)
str_esum = ' '.join(maped_esum)
print(str_esum)

