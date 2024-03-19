def print_list(array, N):
    for i in range(N):
        if i == N-1:
            print(array[i])
        else:
            print(array[i], end=" ")
            
def stable_sort(array_a, array, N):
    for i in range(N-1):
        stable = "yes"
        if array[i][1] == array[i+1][1]:
            index_1 = array.index(array[i])
            index_2 = array.index(array[i+1])
            index_a1 = array_a.index(array[i])
            index_a2 = array_a.index(array[i+1])
            #print(index_1, index_2, index_a1, index_a2)
            if not(index_1 < index_2\
            and index_a1 < index_a2):
                stable = "no"
                break
    if stable == "yes":
        print("Stable")
    else:
        print("Not stable")
            
N = int(input())
a = input().split()
b = [s for s in a]
for i in range(N-1):
    for j in range(N-1, i, -1):
        if b[j][1] < b[j-1][1]:
            t = b[j]
            b[j] = b[j-1]
            b[j-1] = t
print_list(b, N)
stable_sort(a, b, N)

c = [s for s in a]
for i in range(N-1):
    min_i = c[i][1]
    change = "no"
    for j in range(i+1, N):
        if min_i > c[j][1]:
            min_i = c[j][1]
            index = c.index(c[j])
            change = "ok"
    if change == "ok":
        t = c[i]
        c[i] = c[index]
        c[index] = t
print_list(c, N)
stable_sort(a, c, N)