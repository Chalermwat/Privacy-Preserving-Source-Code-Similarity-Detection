input_line = int(input())
out_selection = input().split()
out_bubble = out_selection[:]

# bubblesort                                                                                  
for i in range(input_line):
    for j in range(input_line-1, i, -1):
        if out_bubble[j][1] < out_bubble[j-1][1]:
            out_bubble[j], out_bubble[j-1] = out_bubble[j-1],out_bubble[j]
print(*out_bubble)
print("Stable")

# selectionsort                                                                               
for i in range(input_line):
    minj = i
    for j in range(i, input_line):
        if out_selection[j][1] < out_selection[minj][1]:
            minj = j
    out_selection[i], out_selection[minj] = out_selection[minj], out_selection[i]

print(*out_selection)
print("Stable" if out_bubble == out_selection else "Not stable")
