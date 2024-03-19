import copy 

n = int(input())
c = input().split()
c_sel = copy.deepcopy(c)

# check stability of default array
ord_dict_def = {}
for i in range(n) :
    if int(c[i][1]) in ord_dict_def.keys() :
        ord_dict_def[int(c[i][1])] += c[i][0]
    else :
        ord_dict_def[int(c[i][1])] = c[i][0]
        
# do bubble 
for i in range(n) :
    for j in range(n - 1, i, -1) :
        if int(c[j - 1][1]) > int(c[j][1]) :
            c[j - 1], c[j] = c[j], c[j - 1]

# check stability for bubble
ord_dict_bubble = {}

for i in range(n) :
    if int(c[i][1]) in ord_dict_bubble.keys() :
        ord_dict_bubble[int(c[i][1])] += c[i][0]
    else :
        ord_dict_bubble[int(c[i][1])] = c[i][0]
        
# do selection
for i in range(n) :
    cmin = i
    for j in range(i + 1, n) :
        if int(c_sel[j][1]) < int(c_sel[cmin][1]) :
            cmin = j
            
    if i != cmin :
        c_sel[i], c_sel[cmin] = c_sel[cmin], c_sel[i]

# check stability for selection
ord_dict_selection = {}

for i in range(n) :
    if int(c_sel[i][1]) in ord_dict_selection.keys() :
        ord_dict_selection[int(c_sel[i][1])] += c_sel[i][0]
    else :
        ord_dict_selection[int(c_sel[i][1])] = c_sel[i][0]
        
stability_bubble = "Stable"
stability_selection = "Stable"

for i in ord_dict_bubble.keys() :
    if ord_dict_def[i] != ord_dict_bubble[i] :
        stability_bubble = "Not stable"
        
    if ord_dict_def[i] != ord_dict_selection[i] :
        stability_selection = "Not stable"
        
print(" ".join(c))
print(stability_bubble)
print(" ".join(c_sel))
print(stability_selection)
