def print_list_split_whitespace(a):
    for x in a[:-1]:
        print(x, end=' ')
    print(a[-1])
    
s = list(input())
st1 = []
st2 = []

for index, c in enumerate(s):
    if c == "\\":
        st1.append(index)
    elif c == "/":
        if len(st1) >= 1:
            pop_index = st1.pop()
            area = index - pop_index
            while True:
                if len(st2) >= 1:
                    ind, pop_area = st2.pop()
                else:
                    st2.append((index, area))
                    break
                if ind < pop_index:
                    st2.append((ind, pop_area))
                    st2.append((index, area))
                    break
                else:
                    area += pop_area

a = 0
k = len(st2)
ls = [k]
for _, s in st2:
    a += s
    ls.append(s)

print(a)
print_list_split_whitespace(ls)
